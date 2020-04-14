import unittest

from query.xpath.builder import XPathBuilder


class TestSearchTerms(unittest.TestCase):

    def setUp(self) -> None:
        self.subject = XPathBuilder()

    def test_instance(self):
        xp = self.subject.add_next_node('a', 'test').finalize()
        self.assertEqual(str(xp), "./a[contains(@class, 'test')]")

    def test_length(self):
        xp = self.subject.add_any_descendant_node('a', 'test').finalize()
        self.assertEqual(str(xp), ".//a[contains(@class, 'test')]")
