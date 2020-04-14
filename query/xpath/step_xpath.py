from typing import List

from . import XPath


class StepXPath(XPath):

    def __init__(self, query: List):
        super().__init__()
        self.__query = query

    def as_query(self):
        return "".join(map(lambda x: str(x), self.__query))

    def __str__(self):
        return self.as_query()
