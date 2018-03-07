#!/usr/bin/env python3
# -*- coding: utf8 -*-

# This script allows you to replace hosts and client hosts in gdeploy
# config file, addressing use case described here:
# https://github.com/gluster/gdeploy/issues/422

# To use this script on umsqe server with python3 software collection,
# run it via:
#
# python ./bin/ansible2gdeploy.py -i usm1.hosts \
#   gdeploy_config/volume_alpha_distrep_6x2.create.conf
#
# python ./bin/ansible2gdeploy.py -i usm1.hosts \
#   -p UPDATE_ -s vdb,vdc,vdd,vde,vdf,vdg \
#   gdeploy_config/volume_alpha_distrep_6x2.create.conf \
#   gdeploy_config/volume_beta_arbiter_2_plus_1x2.create.conf \


from configparser import ConfigParser
import argparse
import os
import sys


# names of ansible inventory groups to use
# TODO: make reconfigurable from command line if needed
GLUSTER_SERVER_GROUP = "gluster-servers"
GLUSTER_CLIENT_GROUP = "usm_client"

def parse_args():
    """
    Parse command line arguments.
    """
    ap = argparse.ArgumentParser(
        description="update of hosts and devices in gdeploy conf file")
    ap.add_argument(
        "-d",
        "--dry-run",
        action="store_true",
        help="print to stdout instead of save to file")
    ap.add_argument(
        "gdeployconf",
        nargs="+",
        help="gdeploy config files to edit")
    ap.add_argument(
        "-i",
        dest="inventory",
        action="store",
        help="ansible inventory (aka hosts) file")
    ap.add_argument(
        "-p",
        dest="file_prefix",
        action="store",
        default="",
        help="output file prefix (added before the name of the input gdeploy conf file) " \
            "If empty, input file is overwritten (in place edit).")
    ap.add_argument(
        "-s",
        "--storage-devices",
        dest="storage_devices",
        help="Coma separated list of available devices for bricks.")
    return ap.parse_args()

def main():
    """
    main function
    """
    args = parse_args()

    # open gdeploy config files via plain config parser
    gdeploy_confs = {}
    for gdeploy_conf_file in args.gdeployconf:
        if not os.path.exists(gdeploy_conf_file):
            msg = "Specified gdeploy config file '{}' doesn't exists.".format(
                gdeploy_conf_file)
            print(msg, file=sys.stderr)
            return 1
        gdeploy_confs[gdeploy_conf_file] = ConfigParser(allow_no_value=True)
        gdeploy_confs[gdeploy_conf_file].read(gdeploy_conf_file)

    # open ansible inventory file via plain config parser
    inventory = ConfigParser(allow_no_value=True)
    inventory.read(args.inventory)

    # validate the inventory file
    sections_to_validate = [GLUSTER_SERVER_GROUP]
    if any([gc.has_section("clients") for gc in gdeploy_confs.values()]):
        sections_to_validate.append(GLUSTER_CLIENT_GROUP)
    for section in sections_to_validate:
        if not inventory.has_section(section):
            msg = "inventory file {} is missing group {}".format(
                args.inventory, section)
            print(msg, file=sys.stderr)
            return 1

    # get machines from the inventory file
    servers = inventory.options(GLUSTER_SERVER_GROUP)
    if any([gc.has_section("clients") for gc in gdeploy_confs.values()]):
        clients = inventory.options(GLUSTER_CLIENT_GROUP)
    else:
        clients = []

    # prepare list of storage devices
    storage_devices = []
    if args.storage_devices:
        storage_devices = args.storage_devices.split(",")

    print("servers: " + ", ".join(servers), file=sys.stderr)
    print("clients: " + ", ".join(clients), file=sys.stderr)
    print("devices: " + ", ".join(storage_devices), file=sys.stderr)

    # update gdeploy config files
    for gdeploy_conf_file in gdeploy_confs:
        # ignore hosts section if present
        if gdeploy_confs[gdeploy_conf_file].has_section("hosts"):
            gdeploy_confs[gdeploy_conf_file].remove_section("hosts")
        # add servers into hosts sections
        gdeploy_confs[gdeploy_conf_file].add_section("hosts")
        for server in servers:
            gdeploy_confs[gdeploy_conf_file].set("hosts", server, None)

        # configure client
        if gdeploy_confs[gdeploy_conf_file].has_section("clients"):
            gdeploy_confs[gdeploy_conf_file].set("clients", "hosts", ",".join(clients))

        # configure storage devices
        if args.storage_devices and \
                gdeploy_confs[gdeploy_conf_file].has_section("backend-setup") and \
                gdeploy_confs[gdeploy_conf_file].has_option("backend-setup", "devices"):

            # number of used devices
            n_devices = len(gdeploy_confs[gdeploy_conf_file].get("backend-setup", "devices").split(","))

            if n_devices > len(storage_devices):
                msg = "Not enough storage devices for {} - available: {} ({}), required: {}".format(
                    gdeploy_conf_file, len(storage_devices), ",".join(storage_devices), n_devices)
                print(msg, file=sys.stderr)
                return 1
            gdeploy_confs[gdeploy_conf_file].set("backend-setup", "devices", \
                ",".join(storage_devices[:n_devices]))
            storage_devices = storage_devices[n_devices:]

        # generate and save/print output
        if args.dry_run:
            print("## %s" % gdeploy_conf_file)
            gdeploy_confs[gdeploy_conf_file].write(sys.stdout, space_around_delimiters=False)
        else:
            output_filename = os.path.join(
                os.path.dirname(gdeploy_conf_file),
                "%s%s" % (args.file_prefix, os.path.basename(gdeploy_conf_file)))
            with open(output_filename, 'w') as output_file:
                gdeploy_confs[gdeploy_conf_file].write(output_file, space_around_delimiters=False)


if __name__ == '__main__':
    sys.exit(main())
