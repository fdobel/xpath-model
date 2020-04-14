from structure.search.queries import IncorrectNumberOfResults, Query
from structure.search.result import QueryResult


class SingleSearchQuery(Query):

    def __call__(self, *args, **kwargs):
        res = []
        for idx, element in self.select_from:
            if element.node_contains_text(self.that_contains) or element.contains_link_with(self.that_contains):
                res.append(element)
        return QueryResult(self, res)


class SearchQuerySingleResult(Query):

    def __call__(self, *args, **kwargs):
        res = []
        for idx, element in self.select_from:
            if element.node_contains_text(self.that_contains) or element.contains_link_with(self.that_contains):
                res.append(element)
        if len(res) != 1:
            raise IncorrectNumberOfResults(len(res))
        return QueryResult(self, res)

