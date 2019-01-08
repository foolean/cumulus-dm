#!/usr/bin/env python3
#
# setup.py - Installer for cumulus-dm

from distutils.core import setup

setup(
    name         = 'cumulus-dm',
    version      = '1.0.0',
    description  = 'Cumulus "download manager"',
    author       = 'Bennett Samowich',
    author_email = 'bennett@foolean.org',
    url          = 'https://github.com/foolean/cumulus-dm',
    license      = 'GnuGPLv3',
    packages     = [],
    scripts      = [ 'cumulus-dm' ],
    data_files = [
        ('etc', ['cumulus-dm.conf']),
        ('/usr/share/doc/cumulus-dm', ['README.md', 'COPYING'])
    ]
)
