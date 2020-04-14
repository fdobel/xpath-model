from typing import List


class PlainXPath:

    class Builder:
        class Node:
            def __init__(self, selector, node_name, class_name):
                self._selector = selector
                self.node_name = node_name
                self.class_name = class_name

            def __str__(self):
                if self.class_name == "":
                    return "%s%s" % (self._selector, self.node_name)
                return "%s%s[contains(@class, '%s')]" % (self._selector, self.node_name, self.class_name)

        def __init__(self):
            self.__nodes = []

        @staticmethod
        def from_text(text):
            return PlainXPath(text)

        def add_any_next_node(self, node: str, class_name: str):
            self.__nodes.append(PlainXPath.Builder.Node('.//', node, class_name))
            return self

        def add_next_node(self, node: str, class_name: str):
            self.__nodes.append(PlainXPath.Builder.Node('./', node, class_name))
            return self

        def finalize(self):
            return PlainXPath(self.__nodes)

    def __init__(self, query: List):
        super().__init__()
        self.__query = query

    def as_query(self):
        return "".join(map(lambda x: str(x), self.__query))

    def __str__(self):
        return self.as_query()
