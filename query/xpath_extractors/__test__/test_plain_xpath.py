import unittest

from query.xpath_extractors.plain_xpath import PlainXPath


class TestSearchTerms(unittest.TestCase):

    def setUp(self) -> None:
        self.subject = PlainXPath.Builder()

    def test_instance(self):
        xp = self.subject.add_next_node('a', 'test').finalize()
        self.assertEqual(str(xp), "./a[contains(@class, 'test')]")

    def test_length(self):
        xp = self.subject.add_any_next_node('a', 'test').finalize()
        self.assertEqual(str(xp), ".//a[contains(@class, 'test')]")
