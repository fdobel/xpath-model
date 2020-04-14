
from . import XPath


class PlainXPath(XPath):

    def __init__(self, query: str):
        super().__init__()
        self.__query = query

    def as_query(self):
        return self.__query

    def __str__(self):
        return self.as_query()
