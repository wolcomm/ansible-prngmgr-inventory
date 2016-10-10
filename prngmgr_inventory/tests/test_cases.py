import os
import json
from unittest import TestCase
from prngmgr_inventory import inventory, parser


class TestOutput(TestCase):
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'prngmgr_inventory_test.ini')

    def test_list(self):
        data = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'test_list_data.json')
        cli = ['-f', self.path, '-d', data, '--list']
        args = parser.Parser(args=cli).args
        output = inventory.Inventory(args=args).output
        self.assertTrue(isinstance(json.loads(output), dict))

    def test_host(self):
        host = 'test1.example.net'
        cli = ['-f', self.path, '--host', host]
        args = parser.Parser(args=cli).args
        output = inventory.Inventory(args=args).output
        self.assertTrue(isinstance(json.loads(output), dict))
