import unittest
from types import GeneratorType

from __test__.factories.environments import bbc1
from structure.environment import XPathEnvironment, XPathQueryable

SUBJECT = bbc1


class TestXPathEnvironment(unittest.TestCase):

    def test_environment_init(self):
        self.assertIsInstance(SUBJECT, XPathEnvironment)
        self.assertIsInstance(SUBJECT, XPathQueryable)

    def test_method_node(self):
        self.assertTrue(hasattr(SUBJECT, 'node'))
        # todo

    def test_method_(self):
        self.assertTrue(hasattr(SUBJECT, 'query_node'))
        # todo

    def test_method_iter(self):
        self.assertTrue(hasattr(SUBJECT, 'iter'))
        self.assertIsInstance(SUBJECT.iter(), GeneratorType)

    def test_test(self):
        from structure.nodes.Node import XPathNode

        for a in SUBJECT.iter():
            self.assertIsInstance(a, XPathNode)
            # print(a)


if __name__ == '__main__':
    unittest.main()