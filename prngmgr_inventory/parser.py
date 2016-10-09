import argparse


class Parser(object):
    def __init__(self):
        prog = "prngmgr-inventory"
        description = "An ansible dynamic inventory module to fetch peering session data from prngmgr"
        parser = argparse.ArgumentParser(description=description, prog=prog)
        group = parser.add_mutually_exclusive_group()
        group.add_argument('--list', action='store_true', help="return full inventory data")
        group.add_argument('--host', action='store', nargs=1, type=str, help="return inventory data for HOST")
        self._parser = parser

    @property
    def args(self):
        return self._parser.parse_args()
