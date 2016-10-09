import json
import requests
from prngmgr_inventory import configuration


class Inventory(object):
    def __init__(self, args=None):
        self._config = configuration.Config()
        self._args = args
        self._encoder = json.JSONEncoder()

    @property
    def output(self):
        if self._args:
            if self._args.list:
                data = self._list_data()
            elif self._args.host:
                data = self._host_data(self._args.host)
            else:
                raise ValueError("no valid command-line arguments found")
        else:
            data = self._list_data()
        return self._encoder.encode(data)

    def _list_data(self):
        return {'type': 'list'}

    def _host_data(self, host):
        return {'type': 'host', 'host': host}
