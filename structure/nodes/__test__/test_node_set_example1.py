import unittest

from query.matching.sequence import Sequence
from structure.nodes.Node import XPathNode
from structure.nodes.NodeSet import NodeSet
from test.factories.environment import ENVIRONMENT_EXAMPLE1
ENVIRONMENT = ENVIRONMENT_EXAMPLE1

SUBJECT = NodeSet([])


class TestNodeSet(unittest.TestCase):

    def setUp(self) -> None:
        l1 = list(ENVIRONMENT.select_all_nodes_with_class("div", "test1"))
        l2 = list(ENVIRONMENT.select_all_nodes_with_class("div", "test2"))
        self.node_set = NodeSet(l1 + l2)

    def test_environment_init(self):
        self.assertIsInstance(SUBJECT, NodeSet)

    def test_common_ancestor(self):
        with self.assertRaises(AttributeError):
            SUBJECT.common_ancestor()

    def test_iter(self):
        for node in self.node_set:
            self.assertIsInstance(node, XPathNode)

    def test_select_nodes(self):
        self.assertIsInstance(self.node_set, NodeSet)

    def test_common_ancestor_working(self):
        cas = self.node_set.common_ancestor()
        self.assertIsInstance(cas, Sequence)
        self.assertEqual(
            list(map(lambda a: str(a.value), cas)),
            ['html[]', 'body[]', 'div[wrapper]', 'article[article1]'])

