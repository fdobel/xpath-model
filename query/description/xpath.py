from typing import List

from structure.nodes.Node import XPathNode


class XPath:

    class Step:
        def __init__(self, node: XPathNode):
            self.__node = node

        @staticmethod
        def contains(attribute, query):
            return "contains(@%s, '%s')" % (attribute, query)

        def class_if(self) -> str:
            if self.__node.class_attrib == "":
                return ""
            return "[%s]" % self.contains("class", self.__node.class_attrib)

        def with_classes(self) -> str:
            return "%s%s" % (self.__node.value.tag, self.class_if())

        def without_classes(self) -> str:
            return "%s" % self.__node.value.tag

    def __init__(self, nodes: List[XPathNode]):
        self.__nodes = nodes

    def without_classes(self):
        return "/".join("%s" % XPath.Step(n).without_classes() for n in self.__nodes)
        # return "/".join(n.value.tag for n in self.__nodes)

    def with_classes(self):
        return "/".join("%s" % XPath.Step(n).with_classes() for n in self.__nodes)