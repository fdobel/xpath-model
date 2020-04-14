import unittest
from structure.environment import XPathEnvironment
from structure.nodes.Node import XPathNode

SUBJECT = XPathEnvironment.build().from_file('./test/example_html.dat')


class TestNodeFromEnvironment(unittest.TestCase):

    def test_environment_init(self):
        for node in SUBJECT.select_all_nodes("div"):
            self.assertIsInstance(node, XPathNode)

