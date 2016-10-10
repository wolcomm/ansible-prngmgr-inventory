import os
import json
from unittest import TestCase
from prngmgr_inventory import inventory, parser


class TestOutput(TestCase):
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'prngmgr_inventory_test.ini')
    decoder = json.JSONDecoder()

    def test_list(self):
        cli = ['-f', self.path, '--list']
        args = parser.Parser(args=cli).args
        output = inventory.Inventory(args=args).output
        self.assertTrue(isinstance(self.decoder.decode(output), dict))

    def test_host(self):
        host = 'test.example.net'
        cli = ['-f', self.path, '--host', host]
        args = parser.Parser(args=cli).args
        output = inventory.Inventory(args=args).output
        self.assertTrue(isinstance(self.decoder.decode(output), dict))
