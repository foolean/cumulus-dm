# cumulus-dl - A Cumulus "download manager"

Cumulus is a powerful Open Networking (ON) operating system.  The Cumulus
image files can be downloaded from their website via a manual process.
cumulus-dl was written to automate the downloading of the image files for
cases such as keeping a PXE server up to date with the most current
image files.


## Installation

Run the following to install cumulus-dm:

    python3 setup.py install

Once installed, modify /usr/local/etc/cumulus-dm.conf to suit your needs
   

## Uninstalling

There really isn't a clean uninstall process in Python's setup.py.  However,
the following can be used to uninstall cumulus-dm:

    python3 setup.py install --record files.txt
    cat files.txt | xargs rm -rf
