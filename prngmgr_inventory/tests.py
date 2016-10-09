from unittest import TestCase
import prngmgr_inventory


class TestCli(TestCase):
    def cli_test(self):
        output = prngmgr_inventory.main()
        self.assertTrue(isinstance(output, str))
