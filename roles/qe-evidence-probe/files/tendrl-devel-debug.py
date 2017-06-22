#!/usr/bin/env python2

# Based on *Information required for debugging issues on the Tendrl stack* wiki
# page:
# https://github.com/Tendrl/documentation/wiki/Information-required-for-debugging-issues-on-the-Tendrl-stack

import socket
import subprocess

print "socket.getfqdn() returns:", socket.getfqdn()
print "socket.gethostname() returns:", socket.gethostname()

ip_output = subprocess.check_output(['ip', 'a', 's']).splitlines()
ipv4_nets = [line.strip().split(' ')[1] for line in ip_output if 'global' in line and line.startswith('    inet ')]
for network in ipv4_nets:
    ip_addr, prefix = network.split('/')
    value = socket.gethostbyaddr(ip_addr)
    print "socket.gethostbyaddr({}) returns:".format(ip_addr), value
