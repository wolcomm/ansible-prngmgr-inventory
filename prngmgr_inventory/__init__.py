"""
PrngMgr dynamic inventory module
================================

An ansible dynamic inventory module to fetch peering session data from prngmgr
"""

import os
import ConfigParser
import json
import requests


def main():
    config = _read_config()
    host = config.get("prngmgr", "host")
    port = config.get("prngmgr", "port")
    output = "connecting to prngmgr at %s:%s" % (host, port)
    return output


def _read_config():
    config = ConfigParser.SafeConfigParser()
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'prngmgr_inventory.ini')
    config.read(path)
    return config
