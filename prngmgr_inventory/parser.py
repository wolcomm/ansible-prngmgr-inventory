import argparse


class Parser(object):
    def __init__(self, args=None):
        program_name = "prngmgr-inventory"
        description = "An ansible dynamic inventory module to fetch peering session data from prngmgr"
        parser = argparse.ArgumentParser(description=description, prog=program_name)
        parser.add_argument('-f', action='store', dest='path', type=str, help="path to configuration file")
        group = parser.add_mutually_exclusive_group()
        group.add_argument('--list', action='store_true', help="return full inventory data")
        group.add_argument('--host', action='store', type=str, help="return inventory data for HOST")
        self._parser = parser
        self._args = args

    @property
    def args(self):
        if self._args:
            return self._parser.parse_args(self._args)
        else:
            return self._parser.parse_args()
