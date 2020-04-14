import unittest
from os import path

from query.matching.sequence import Sequence

SUBJECT = Sequence([1, 2, 3])
SUBJECT_ = Sequence([1, 2, 3])
SUBJECT2 = Sequence([2, 3, 4])


class TestSequence(unittest.TestCase):
    def test_init(self):
        self.assertIsInstance(SUBJECT, Sequence)

    @unittest.skip("pending")
    def test_eq(self):
        self.assertEqual(SUBJECT, SUBJECT_)

    @unittest.skip("pending")
    def test_ineq(self):
        self.assertNotEqual(SUBJECT, SUBJECT2)


