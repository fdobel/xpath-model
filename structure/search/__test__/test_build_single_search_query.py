
import unittest

from structure.search.queries import IncorrectNumberOfResults
from structure.search.single_search_query import SearchQuerySingleResult

from structure.search.result import QueryResult
from test.factories.environment import ENVIRONMENT_EXAMPLE1, ENVIRONMENT_EXAMPLE2


class TestMSQ(unittest.TestCase):

    def test_init(self):
        SUBJECT = SearchQuerySingleResult.build()
        self.assertIsInstance(SUBJECT, SearchQuerySingleResult.Builder)

    def test_build(self):
        environment = [] # todo make it a nice input
        terms = ""
        SUBJECT = SearchQuerySingleResult.build().select_from(environment).that_contains(terms)
        self.assertIsInstance(SUBJECT, SearchQuerySingleResult.Builder)

    def test_finalize(self):
        environment = [] # todo make it a nice input
        terms = ""
        SUBJECT = SearchQuerySingleResult.build()\
            .select_from(environment)\
            .that_contains(terms)\
            .finalize()
        self.assertIsInstance(SUBJECT, SearchQuerySingleResult)

    def test_call_query_environment_1(self):
        environment = enumerate(ENVIRONMENT_EXAMPLE1.iter())
        terms = "a"  # todo
        SUBJECT = SearchQuerySingleResult.build() \
            .select_from(environment) \
            .that_contains(terms) \
            .finalize()
        query_result = SUBJECT()
        self.assertIsInstance(query_result, QueryResult)
        self.assertEqual(str(query_result), "<QueryResult #results:1 results:div[test test1] >")

    def test_call_query_environment_2(self):
        environment = enumerate(ENVIRONMENT_EXAMPLE2.iter())
        terms = "a"  # todo
        with self.assertRaises(IncorrectNumberOfResults):
            SUBJECT = SearchQuerySingleResult.build() \
                .select_from(environment) \
                .that_contains(terms) \
                .finalize()
            SUBJECT()
