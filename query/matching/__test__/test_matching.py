import unittest

from query.matching.sequence import Sequence


class TestMatching(unittest.TestCase):

    def setUp(self) -> None:
        self.equal = lambda a, b: a == b
        equal = self.equal
        self.s1 = Sequence([1, 2, 3, 5, 6, 9], elements_equal=equal)
        self.s2 = Sequence([1, 2, 5, 6, 9], elements_equal=equal)
        self.s3 = Sequence([1, 2], elements_equal=equal)
        self.s4 = Sequence([1, 2], elements_equal=equal)
        self.s5 = Sequence([1, 5, 6, 9], elements_equal=equal)
        self.s6 = Sequence([5, 6, 9], elements_equal=equal)

    def test_matching1(self):
        self.assertEqual(self.s1.match_longest_start_sequence(self.s2), Sequence([1, 2], elements_equal=self.equal))
        self.assertFalse(self.s1.compare(self.s2))

    def test_matching2(self):
        self.assertEqual(self.s3.match_longest_start_sequence(self.s4), Sequence([1, 2], elements_equal=self.equal))
        self.assertTrue(self.s3.compare(self.s4))

    def test_matching3(self):
        self.assertEqual(self.s4.match_longest_start_sequence(self.s5), Sequence([1], elements_equal=self.equal))

    def test_matching4(self):
        self.assertEqual(self.s5.match_longest_start_sequence(self.s6), Sequence([], elements_equal=self.equal))




