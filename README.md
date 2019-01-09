# cumulus-dl - A Cumulus "download manager"

Cumulus is a powerful Open Networking (ON) operating system.  The Cumulus
image files can be downloaded from their website via a manual process.
cumulus-dl was written to automate the downloading of the image files for
cases such as keeping a PXE server up to date with the most current
image files.


## Dependencies

### debian/ubuntu

    python-configparser
    python3-bs4
    python-requests
    python3-requests
    python3-urllib3

### CentOS/RedHat

    python-configparser
    python-beautifulsoup4
    python-requests
    python-urllib3

## Installation

Run the following to install cumulus-dm:

    python3 setup.py install

Once installed, modify /usr/local/etc/cumulus-dm.conf to suit your needs

Note: if not specified via -C cumulus-dm will look for the configuration file in:
    1) /etc/cumulus-dm.conf
    2) /usr/local/etc/cumulus-dm.conf

## Uninstalling

There really isn't a clean uninstall process in Python's setup.py.  However,
the following can be used to uninstall cumulus-dm:

    python3 setup.py install --record files.txt
    cat files.txt | xargs rm -rf

## Usage

	Usage: cumulus-dm [options]

	Options:
  	--version               show program's version number and exit
  	-h, --help              show this help message and exit
  	-c CPU, --cpu=CPU       Filter image files by cpu type
  	-C CONFIG-FILE, --config=CONFIG-FILE
                        	Specify an alternate configuration file [default=none]
  	-d DESTINATION, --destination=DESTINATION
                        	Destination directory to save image files to
  	-D, --debug             Print extra debugging information (implies --verbose)
  	-p PRODUCT, --product=PRODUCT
                        	Filter image files by product
  	-q, --quiet             Suppress output (negates --debug and --verbose)
  	-s SOC, --soc=SOC       Filter image files by chipset
  	-v VERSION, --product-version=VERSION
                        	Filter image files by version number

    Note:
    cpu is limited to:     'x86', 'PowerPC', 'ARM' 
    soc is limited to:     'Broadcom', 'Mellanox'
    product is limited to: 'Cumulus Linux', 'NetQ Virtual', 'Cumulus VX'

