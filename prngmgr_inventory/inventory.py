import json
import requests
from prngmgr_inventory import configuration


class Inventory(object):
    def __init__(self, args=None):
        self._args = args
        if self.args:
            path = self.args.path
        else:
            path = None
        self._config = configuration.Config(path=path)

    @property
    def config(self):
        return self._config

    @property
    def args(self):
        return self._args

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
        return json.dumps(data, indent=4)

    def _list_data(self):
        if self._args.data:
            data = self._local_query(self._args.data)
        else:
            url = "http://%s:%s/api/router/" % (self.config.get('host'), self.config.get('port'))
            data = self._api_query(url=url)
        return data

    def _host_data(self, host):
        return {'type': 'host', 'host': host}

    def _api_query(self, url=None):
        if self.config.get('user'):
            auth=(
                self.config.get('user'),
                self.config.get('password')
            )
        else:
            auth = None
        try:
            response = requests.get(url, auth=auth)
            response.raise_for_status()
        except requests.RequestException:
            raise
        return response.json()

    def _local_query(self, path=None):
        if path:
            try:
                with open(path) as f:
                    return json.loads(f.read())
            except Exception:
                raise
        else:
            raise ValueError
