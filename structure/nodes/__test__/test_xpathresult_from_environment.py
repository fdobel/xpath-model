import unittest
from structure.environment import XPathEnvironment
from structure.nodes.XPathResult import XPathResult

SUBJECT = XPathEnvironment.build().from_file('./test/example_html.dat')


class TestXPathResultFromEnvironment(unittest.TestCase):

    def test_environment_init(self):
        self.assertIsInstance(SUBJECT.select_all_nodes("div"), XPathResult)

