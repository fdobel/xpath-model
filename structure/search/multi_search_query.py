from .result import MultiQueryResult
from .single_search_query import SingleSearchQuery
from .queries import Query, IncorrectNumberOfResults


class MultiSearchQuery(Query):

    def __call__(self, *args, **kwargs):
        res = []
        for search_term in self.that_contains:

            query = SingleSearchQuery.build()\
                .select_from(self.select_from)\
                .that_contains(search_term)\
                .finalize()
            try:
                query_result = query()
                res.append(query_result)
            except IncorrectNumberOfResults as error:
                # print(error)
                pass
                # self.missing += 1

        # self.called = True
        return MultiQueryResult(self, res)
