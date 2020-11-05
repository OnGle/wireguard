'''Helper script for wireguard-addclient'''

import os
from subprocess import Popen, CalledProcessError, PIPE, check_output

TITLE = "Add client"

def run():
    while True:
        rty, name = console.inputbox(TITLE, "Enter name")
        if rty == 'cancel': break

        rte, traffic_cidr = console.inputbox(TITLE, "Enter traffic CIDR to route into VPN")
        if rte == 'ok' and rty == 'ok':
            proc = Popen(["wireguard-addclient", name, traffic_cidr],
                stderr=PIPE, stdout=PIPE, text=True)
            out, err = proc.communicate()
            returncode = proc.returncode
            if returncode == 0:
                console.msgbox(TITLE, '{} ({})'.format(out, name))
            else:
                console.msgbox(TITLE, '{} ({})'.format(err, name))
            break
        else:
           break
