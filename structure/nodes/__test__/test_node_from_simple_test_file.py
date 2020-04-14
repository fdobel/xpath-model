import unittest
from structure.environment import XPathEnvironment
from structure.nodes.Node import XPathNode
from structure.nodes.NodeValue import NodeValue
from structure.nodes.Position import Position

SUBJECT = XPathEnvironment.build().from_file('./structure/nodes/__test__/node.html')
NODE = list(SUBJECT.select_all_nodes("div"))[0]


class TestNodeFromEnvironment(unittest.TestCase):

    def test_environment_single_node(self):
        self.assertIsInstance(NODE, XPathNode)
        assert hasattr(NODE, "xpath")
        assert hasattr(NODE, "iter")

    # node value
    def test_node_value(self):
        value = NODE.value
        self.assertIsInstance(value, NodeValue)

    def test_node_tag(self):
        value = NODE.value
        self.assertEqual(NODE.tag, NODE.value.tag)
        self.assertEqual(value.tag, "div")

    def test_node_class_attrib(self):
        value = NODE.value
        self.assertEqual(NODE.class_attrib, NODE.value.class_attrib)
        self.assertEqual(value.class_attrib, "wrapper")

    def test_node_attrib(self):
        value = NODE.value
        self.assertEqual(NODE.attrib, NODE.value.attrib)
        self.assertEqual(value.attrib, {'class': 'wrapper'})

    def test_node_href(self):
        value = NODE.value
        self.assertEqual(NODE.href, NODE.value.href)
        self.assertEqual(value.href, None)

    def test_node_text(self):
        value = NODE.value
        self.assertEqual(NODE.text, NODE.value.text)
        self.assertEqual(value.text.strip(), "")

    def test_node_str(self):
        self.assertEqual(NODE.to_s(), "<<class 'structure.nodes.Node.XPathNode'> value: div[wrapper]>")

    def test_node_value_str(self):
        value = NODE.value
        self.assertEqual(str(value), "div[wrapper]")

    def test_node_contains_text(self):
        self.assertEqual(NODE.node_contains_text("test"), False)

    def test_node_concat_texts(self):
        text = NODE.concat_texts()
        self.assertEqual(text, '  a b c d ')

    def test_ancestors(self):
        position = Position.ancestors(NODE)
        self.assertIsInstance(position, Position)


