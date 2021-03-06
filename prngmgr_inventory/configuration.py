import os
import ConfigParser


class Config(object):
    def __init__(self, path=None):
        config = ConfigParser.SafeConfigParser()
        if not path or not os.path.isfile(path):
            path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'prngmgr_inventory.ini')
        config.read(path)
        self._config = config

    def get(self, key=None):
        try:
            value = self._config.get("prngmgr", key)
        except:
            value = None
        return value
