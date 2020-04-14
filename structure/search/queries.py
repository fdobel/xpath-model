class IncorrectNumberOfResults(Exception):

    def __init__(self, no):
        self.no = no

    def __str__(self):
        return "Expected 1. Got: %d" % self.no


class Query:

    class Builder:
        def __init__(self, class_to_build):
            self.__select_from = None
            self.__that_contains = None
            self.class_to_build = class_to_build

        def select_from(self, select_from):
            """

            :param select_from: enumerated iterator
            :return: self
            """
            self.__select_from = select_from
            return self

        @property
        def iterator(self):
            return self.__select_from

        def that_contains(self, value):
            """

            :param value: string instance - string that is searched
            :return:
            """
            self.__that_contains = value
            return self

        def finalize(self):
            return self.class_to_build(self.iterator, self.__that_contains)
        pass

    def __init__(self, select_from, that_contains):
        self.select_from = select_from
        self.that_contains = that_contains

    @classmethod
    def build(cls):
        return Query.Builder(cls)


"""
class SearchQuery(Query):

    def __call__(self, *args, **kwargs):
        res = []
        for idx, element in self.iterator:
            if element.node_contains_text(self.contains):
                res.append(element)

        return QueryResult(self, res)
"""
