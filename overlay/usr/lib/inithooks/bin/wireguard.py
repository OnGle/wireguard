#!/usr/bin/python3
"""Initialize Wireguard server keys and configuration

Server profile options:

    --virtual-subnet=   IP address of server and range of virtual subnet
                        in CIDR notation
    --domain=           domain (or ip) which will be given to the client
                        to use as the wireguard endpoint.
"""

import os
import sys
import getopt
import inithooks_cache

from dialog_wrapper import Dialog
import subprocess

def fatal(e):
    print('Error:', e, file=sys.stderr)
    sys.exit(1)

def usage(e=None):
    if e:
        print('Error:', e, file=sys.stderr)
    print(f"Syntax: {sys.argv[0]} [options]", file=sys.stderr)
    print(__doc__, file=sys.stderr)
    sys.exit(1)

def main():
    try:
        opts, args = getopt.gnu_getopt(sys.argv[1:], "h",
                ['help', 'virtual-subnet=', 'domain='])
    except getopt.GetoptError as e:
        usage(e)

    virtual_subnet = ""
    domain = ""

    for opt, val in opts:
        if opt in ('-h', '--help'):
            usage()
        elif opt == '--virtual-subnet':
            virtual_subnet = val

    dialog = Dialog("TurnKey Linux - First boot configuration")

    if not virtual_subnet:
        virtual_subnet = dialog.get_input(
                "Wireguard Public Address",
                "Enter IP address in CIDR of server reachable by clients",
                "10.0.0.0/8")


    if not domain:
        domain = dialog.get_input(
                "Wireguard domain",
                "Used in client configuration as wireguard endpoint",
                "www.example.com")
    
    cmd = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'wireguard-server-init.sh')
    subprocess.run([cmd, virtual_subnet, domain])

if __name__ == '__main__':
    main()
