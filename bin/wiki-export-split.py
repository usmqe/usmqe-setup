#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
wiki-export-split: split wikipedia xml dump into plain text files
"""

# Copyright (C) 2014 Martin Bukatovič <martin.bukatovic@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import os
import re
import sys
import xml.sax
from optparse import OptionParser
from tempfile import NamedTemporaryFile


def base36to16(checksum):
    """
    Convert sha1 checksum from base36 form into base16 form.
    """
    return "%040x" % int(checksum, 36)


class StopWikiProcessing(Exception):
    pass


class WikiPageDumper(object):
    """
    Wiki page file dumper.
    """

    def __init__(self, ignore_redirect=False, max_files=None, re_title=None,
        naming_scheme=None, checksum_file=None,
        ):
        self.id = None
        self.title = None
        self.sha1sum = None
        self._file = None
        self._ignore_redirect = ignore_redirect
        self._file_deleted = False
        self._file_count = 0
        self._file_max = max_files
        self._naming_scheme = naming_scheme
        self._re_title = re_title
        self._checksum_file = checksum_file

    def start(self):
        self.id = None
        self.title = None
        self.sha1sum = None
        self._file_count += 1
        self._file_deleted = False
        if self._file_max is not None and self._file_count > self._file_max:
            raise StopWikiProcessing()
        self._file = NamedTemporaryFile(suffix=".wikitext", dir=os.getcwd(), delete=False)

    def _ignore_current_page(self):
        """
        Flag file of current page for deletion and unlink it.
        """
        os.unlink(self._file.name)
        self._file_count -= 1
        self._file_deleted = True

    def write(self, content):
        if self._file_deleted:
            return
        # ignore pages not matching regexp if needed
        if self._re_title is not None and self.title is not None:
            if not self._re_title.search(self.title):
                self._ignore_current_page()
                return
        # ignore redirect pages if needed
        content_header = content[:9].upper()
        if self._ignore_redirect and content_header.startswith('#REDIRECT'):
            self._ignore_current_page()
            return
        self._file.write(content.encode("utf8"))

    def end(self):
        self._file.close()
        # rename file based on selected naming scheme (default: do nothing)
        new_name = None
        if self._naming_scheme == "title" and self.title is not None:
            new_name = self.title
        elif self._naming_scheme == "id" and self.id is not None:
            new_name = self.id
        elif self._naming_scheme == "sha1" and self.sha1sum is not None:
            new_name = self.sha1sum
        if new_name is not None and not self._file_deleted:
            new_name = "{0}.wikitext".format(new_name)
            full_new_name = os.path.join(
                os.path.dirname(self._file.name), new_name)
            try:
                os.rename(self._file.name, full_new_name)
            except OSError, ex:
                msg = "error: file {0} can't be renamed to {1}\n"
                sys.stderr.write(msg.format(self._file.name, full_new_name))
        # if requested, write sha1sum of current page into dedicated file
        if self._checksum_file is not None and not self._file_deleted:
            basename = new_name or os.path.basename(self._file.name)
            line = "{0}  {1}\n".format(base36to16(self.sha1sum), basename)
            self._checksum_file.write(line)


class WikiPageHandler(xml.sax.ContentHandler):
    """
    Page extracting SAX handler.
    Expected input: pages-articles.xml file (full xml dump of wikipedia pages)
    """

    # See Wikipedia pages:
    # https://meta.wikimedia.org/wiki/Help:Export#Export_format
    # https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles.xml.bz2

    def __init__(self, page_dumper):
        xml.sax.ContentHandler.__init__(self)
        self._inside_page = False
        self._curr_elem = None
        self.page = page_dumper

    def startElement(self, name, attrs):
        if name == "page":
            self._inside_page = True
            self.page.start()
            return
        if not self._inside_page:
            return
        self._curr_elem = name

    def endElement(self, name):
        if name == "page":
            self._inside_page = False
            self.page.end()
        self._curr_elem = None

    def characters(self, content):
        if not self._inside_page:
            return
        if self._curr_elem == "id":
            self.page.id = content
        elif self._curr_elem == "title":
            self.page.title = content
        elif self._curr_elem == "sha1":
            self.page.sha1sum = content
        elif self._curr_elem == "text":
            self.page.write(content)


def process_xml(xml_file, opts):
    """
    Process xml file with wikipedia dump.
    """
    # compile regular expression
    try:
        if opts.filter_title is not None:
            re_title = re.compile(opts.filter_title)
        else:
            re_title = None
    except re.error, ex:
        msg = "error: invalid regexp: {0}\n"
        sys.stderr.write(msg.format(ex))
        return 1
    # create file for list of sha1 checksums
    try:
        if opts.sha1sum is not None:
            checksum_file = open(opts.sha1sum, mode="w")
        else:
            checksum_file = None
    except IOError, ex:
        msg = "error: can't create checksum file: {0}\n"
        sys.stderr.write(msg.format(ex))
        return 1
    page_dumper = WikiPageDumper(
        ignore_redirect=opts.noredir,
        max_files=opts.max_files,
        naming_scheme=opts.filenames,
        re_title=re_title,
        checksum_file=checksum_file,
        )
    parser = xml.sax.make_parser()
    parser.setContentHandler(WikiPageHandler(page_dumper))
    try:
        parser.parse(xml_file)
    except StopWikiProcessing, ex:
        pass
    if checksum_file is not None:
        checksum_file.close()

def main(argv=None):
    op = OptionParser(usage="usage: %prog [options] [wikixml]")
    op.add_option("--noredir", action="store_true", help="ignore redirection pages")
    op.add_option("--max-files", help="maximum number of output files", metavar="NUM", type="int")
    op.add_option("--filenames", help="naming scheme for output files", metavar="SCHEME", choices=('id', 'title', 'sha1', 'random'))
    op.add_option("--filter-title", help="save page only if it's title matches given regexp", metavar="RE")
    op.add_option("--sha1sum", help="save sha1 checksums into FILE", metavar="FILE")
    opts, args = op.parse_args()

    if len(args) == 0:
        return process_xml(sys.stdin, opts)
    else:
        with open(args[0], "r") as fobj:
            return process_xml(fobj, opts)

if __name__ == '__main__':
    sys.exit(main())
