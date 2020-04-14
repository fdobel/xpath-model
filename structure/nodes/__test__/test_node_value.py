import unittest
from structure.nodes.NodeValue import NodeValue

SUBJECT = NodeValue("div", { 'class': '' }, "test text... hello world")


class TestNodeValue(unittest.TestCase):

    def test_environment_init(self):
        self.assertIsInstance(SUBJECT, NodeValue)

    def test_node_attributes(self):
        self.assertTrue(hasattr(SUBJECT, 'tag'))
        self.assertTrue(hasattr(SUBJECT, 'attrib'))
        self.assertTrue(hasattr(SUBJECT, 'text'))

    def test_equal_method(self):
        s2 = NodeValue("div", {"class": ''}, "test text... hello world")
        self.assertTrue(SUBJECT, s2)

    def test_str(self):
        self.assertEqual(str(SUBJECT), "div[]")

