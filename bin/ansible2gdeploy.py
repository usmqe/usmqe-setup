#!/usr/bin/env python3
# -*- coding: utf8 -*-

# This script allows you to replace hosts and client hosts in gdeploy
# config file, addressing use case described here:
# https://github.com/gluster/gdeploy/issues/422

# To use this script on umsqe server with python3 software collection,
# run it via:
#
# python ./bin/ansible2gdeploy.py -i usm1.hosts gdeploy_config/volume_usmqe_alpha_distrep_4x2.create.conf


from configparser import ConfigParser
import argparse
import sys


# names of ansible inventory groups to use
# TODO: make reconfigurable from command line if needed
GLUSTER_SERVER_GROUP = "gluster"
GLUSTER_CLIENT_GROUP = "usm_client"


def main():
    ap = argparse.ArgumentParser(
        description="in place update of hosts in gdeploy conf file")
    ap.add_argument(
        "-d",
        "--dry-run",
        action="store_true",
        help="print to stdout instead of in place edit")
    ap.add_argument("gdeployconf", help="gdeploy config file to edit")
    ap.add_argument(
        "-i",
        dest="inventory",
        action="store",
        help="ansible inventory (aka hosts) file")
    ap.add_argument(
        "-o",
        dest="output",
        action="store",
        help="save the result into output file instead of in place edit")
    args = ap.parse_args()

    # open gdeploy config file via plain config parser
    gdeploy_conf = ConfigParser(allow_no_value=True)
    gdeploy_conf.read(args.gdeployconf)

    # open ansible inventory file via plain config parser
    inventory = ConfigParser(allow_no_value=True)
    inventory.read(args.inventory)

    # validate the inventory file
    sections_to_validate = [GLUSTER_SERVER_GROUP]
    if gdeploy_conf.has_section("clients"):
        sections_to_validate.append(GLUSTER_CLIENT_GROUP)
    for section in sections_to_validate:
        if not inventory.has_section(section):
            msg = "inventory file {} is missing group {}".format(
                args.inventory, section)
            print(msg, file=sys.stderr)
            return 1

    # get machines from the inventory file
    servers = inventory.options(GLUSTER_SERVER_GROUP)
    if gdeploy_conf.has_section("clients"):
        clients = inventory.options(GLUSTER_CLIENT_GROUP)
    else:
        clients = []
    print("servers: " + ", ".join(servers), file=sys.stderr)
    print("clients: " + ", ".join(clients), file=sys.stderr)

    # ignore hosts section if present
    if gdeploy_conf.has_section("hosts"):
        gdeploy_conf.remove_section("hosts")
    # add servers into hosts sections
    gdeploy_conf.add_section("hosts")
    for server in servers:
        gdeploy_conf.set("hosts", server, None)

    if gdeploy_conf.has_section("clients"):
        gdeploy_conf.set("clients", "hosts", ",".join(clients))

    if args.dry_run:
        gdeploy_conf.write(sys.stdout)
    else:
        if args.output is not None:
            output_filename = args.output
        else:
            output_filename = args.gdeployconf
        with open(output_filename, 'w') as gdeploy_conf_file:
            gdeploy_conf.write(gdeploy_conf_file)


if __name__ == '__main__':
    sys.exit(main())
