VPN solution built with WireGuard® - Next Generation Open Source VPN
====================================================================

`WireGuard®`_ is an extremely simple yet fast and modern VPN that
utilizes state-of-the-art cryptography. It aims to be faster, simpler,
leaner, and more useful than IPsec, while avoiding the massive headache.
It intends to be considerably more performant than OpenVPN.

The TurnKey Linux VPN software appliance leverages the open source
WireGuard® software (installed from Debian repositories). It also has
custom TurnKey configuration tools to support ease of setup. It can 
link 2 otherwise unconnected LANs and/or secure traffic across public
and/or insecure wifi connections and/or provide a secure solution for
remote work scenarios.

This appliance includes all the standard features in `TurnKey Core`_,
and on top of that:

- WireGuard® configurations:

    - Initialization hooks to configure common WireGuard® deployments,
      server key and confgiuration.
    - Deployments include convenience scripts to add clients/profiles,
      generating all required config.
    - Expiring obfuscated HTTPS urls can be created for clients to
      download their profiles (especially useful with mobile devices
      using a QR code scanner).

See the `Set up documentation`_ for further details.

**Note**: WireGuard® and the "WireGuard" logo are registered trademarks of
Jason A. Donenfeld. TurnKey Linux is not affiliated with Jason A. Donenfeld
or `WireGuard®`_. Neither this software appliance, or the TurnKey provided,
custom configuration scripts are endorsed by Jason A. Donenfeld or
`WireGuard®`_.

Credentials *(passwords set at first boot)*
-------------------------------------------

-  Webmin, SSH: username **root**

.. _WireGuard®: https://www.wireguard.com/
.. _TurnKey Core: https://www.turnkeylinux.org/core
.. _Set up documentation: https://github.com/turnkeylinux-apps/wireguard/blob/master/docs/setup.rst
