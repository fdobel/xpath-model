import unittest



# MultiSearchQuery.build().select_from(found_items).that_contains(terms).finalize()
from structure.search.multi_search_query import MultiSearchQuery
from structure.search.result import MultiQueryResult
from test.factories.environment import ENVIRONMENT_EXAMPLE1


class TestMSQ(unittest.TestCase):

    def test_init(self):
        SUBJECT = MultiSearchQuery.build()
        self.assertIsInstance(SUBJECT, MultiSearchQuery.Builder)

    def test_build(self):
        environment = [] # todo make it a nice input
        terms = 'asdf' # todo
        SUBJECT = MultiSearchQuery.build().select_from(environment).that_contains(terms)
        self.assertIsInstance(SUBJECT, MultiSearchQuery.Builder)

    def test_finalize(self):
        environment = [] # todo make it a nice input
        terms = "test" # todo
        SUBJECT = MultiSearchQuery.build()\
            .select_from(environment)\
            .that_contains(terms)\
            .finalize()
        self.assertIsInstance(SUBJECT, MultiSearchQuery)

    def test_call_query_environment_2(self):
        environment = enumerate(ENVIRONMENT_EXAMPLE1.iter())
        terms = ["a", "b", "c"]  # todo
        SUBJECT = MultiSearchQuery.build() \
            .select_from(environment) \
            .that_contains(terms) \
            .finalize()
        query_result = SUBJECT()
        self.assertIsInstance(query_result, MultiQueryResult)
        self.assertEqual(str(query_result), "<MultiQueryResult #results:3 results:<QueryResult #results:1 results:div[test test1] >,<QueryResult #results:0 results: >,<QueryResult #results:0 results: > >")