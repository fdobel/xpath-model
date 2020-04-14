import unittest

# from automatic_query_creation.matching.sequence import Sequence
from structure.nodes.NodeSet import NodeSet
from test.factories.environment import ENVIRONMENT_EXAMPLE2

ENVIRONMENT = ENVIRONMENT_EXAMPLE2

SUBJECT = NodeSet([])


class TestNodeSet(unittest.TestCase):

    def setUp(self) -> None:
        self.node_list = list(ENVIRONMENT.select_all_nodes_with_class("div", "test"))
        self.node_set = NodeSet(self.node_list)

    def test_iter(self):
        self.assertEqual(len(self.node_list), 8)

    def test_common_ancestor_working(self):
        cas = self.node_set.common_ancestor()
        # self.assertIsInstance(cas, Sequence)
        self.assertEqual(
            list(map(lambda a: str(a.value), cas)),
            ['html[]', 'body[]', 'div[wrapper]'])



