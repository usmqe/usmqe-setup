=================================
 qe-evidence-probe-journald role
=================================

This ansible role automates and standardizes the way QE team extracts
information from journald log database.

Description
-----------

This role creates temporary directory ``/tmp/journald-export/`` on a remote
machine and stores there plain text files in `Journal Export Format`_ for every
systemd service listed in ``evidence_journal_services`` variable.

See `systemd.journal-fields man page`_ for full descrition of Journal Fields
used in the export format.

.. _`Journal Export Format`: https://www.freedesktop.org/wiki/Software/systemd/export/
.. _`systemd.journal-fields man page`: https://www.freedesktop.org/software/systemd/man/systemd.journal-fields.html
