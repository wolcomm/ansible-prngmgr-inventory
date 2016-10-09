#!/usr/bin/env python
'''
PrngMgr dynamic inventory script
================================

An ansible dynamic inventory module to fetch peering session data from prngmgr
'''

import os
import ConfigParser
import json
import requests


def main():
    config = read_config()
    host = config.get("prngmgr", "host")
    port = config.get("prngmgr", "port")
    print "connecting to prngmgr at %s:%s" % (host, port)
    exit()


def read_config():
    config = ConfigParser.SafeConfigParser()
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'prngmgr_inventory.ini')
    config.read(path)
    return config

if __name__ == "__main__":
    main()
