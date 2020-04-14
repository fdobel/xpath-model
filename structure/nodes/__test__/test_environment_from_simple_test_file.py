import unittest
from structure.environment import XPathEnvironment
from structure.nodes.Node import XPathNode
from structure.nodes.Position import Position

SUBJECT = XPathEnvironment.build().from_file('./structure/nodes/__test__/node.html')
LIST_SUBJECT = list(SUBJECT.select_all_nodes("div"))

NODE0 = list(SUBJECT.select_all_nodes("div"))[0]
NODE1 = list(SUBJECT.select_all_nodes("div"))[1]
NODE2 = list(SUBJECT.select_all_nodes("div"))[2]
NODE3 = list(SUBJECT.select_all_nodes("div"))[3]
NODE4 = list(SUBJECT.select_all_nodes("div"))[4]


class TestNodeFromEnvironment(unittest.TestCase):

    def test_environment_type(self):
        self.assertIsInstance(SUBJECT, XPathEnvironment)

    def test_environment_init(self):
        for node in LIST_SUBJECT:
            self.assertIsInstance(node, XPathNode)

    def test_environment_node_length(self):
        self.assertEqual(
            len(LIST_SUBJECT), 5
        )

    def test_environment_single_node(self):
        self.assertFalse(NODE0 == NODE1)

    def test_descendant(self):
        self.assertTrue(Position.is_descendant_of(NODE1, NODE0))





