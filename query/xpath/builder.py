from typing import Dict

from query.xpath.plain_xpath import PlainXPath
from query.xpath.step_xpath import StepXPath
from query.xpath.syntax import SELF_ABBREV, DESCENDANTS_ABBREV

from . import syntax


class XPathBuilder:
    class Node:
        def __init__(self, selector, node_name, contains: Dict):
            self._selector = selector
            self.node_name = node_name
            self._contains = contains

        def __str__(self):
            if len(self._contains) == 0:
                return "%s%s" % (self._selector, self.node_name)
            return "%s%s[%s]" % (self._selector, self.node_name, syntax.contains_n('@class', self._contains['class']))

    def __init__(self):
        self.__nodes = []

    def add_any_descendant_node(self, node: str, class_name: str):
        self.__nodes.append(XPathBuilder.Node('%s%s' % (SELF_ABBREV, DESCENDANTS_ABBREV), node, {'class': class_name}))
        return self

    def add_next_node(self, node: str, class_name: str):
        self.__nodes.append(XPathBuilder.Node('./', node, { 'class': class_name }))
        return self

    @staticmethod
    def from_text(text):
        return PlainXPath(text)

    def finalize(self):
        return StepXPath(self.__nodes)