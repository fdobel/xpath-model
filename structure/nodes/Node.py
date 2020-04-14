import types
from abc import abstractmethod

from .Queryable import XPathQueryable
from .NodeValue import NodeValue
from .XPathResult import XPathResult
# from .Position import Position


class NodeXPathResult(XPathResult):

    def __iter__(self):
        for a in self.xpath_result:
            yield XPathNode(a)


class AbstractNode(XPathQueryable):

    def __init__(self, node):
        if isinstance(node, AbstractNode):
            raise Exception("wrong type")
        self._node = node

    def xpath(self, query) -> NodeXPathResult:
        return NodeXPathResult(self.node.xpath(query))

    @property
    def node(self):
        return self._node

    @abstractmethod
    def iter(self) -> types.GeneratorType:
        raise NotImplementedError("abstract")

    @abstractmethod
    def value(self) -> NodeValue:
        raise NotImplementedError("abstract")

    def to_s(self):
        return "<%s value: %s>" % (self.__class__, self.value)

    def iterancestors(self):
        for a in self.node.iterancestors():
            yield a

    def __eq__(self, other):
        return self.node == other.node


class XPathNode(AbstractNode):

    def iter(self) -> types.GeneratorType:
        for a in self.node.iter():
            yield self.__class__(a)

    @property
    def value(self) -> NodeValue:
        return NodeValue(self.node.tag, self.node.attrib, self.node.text)

    @property
    def tag(self):
        return self.value.tag

    @property
    def class_attrib(self):
        return self.value.class_attrib

    @property
    def href(self):
        return self.value.href

    @property
    def attrib(self):
        return self.value.attrib

    @property
    def text(self):
        return self.value.text

    def concat_texts(self) -> str:
        text = ''
        for node in self.iter():

            if node.text is not None:
                text += "%s " % str(node.text.strip())  # .encode('unicode_escape')

        return text

    def node_contains_text(self, search_text):
        """

        :param search_text:
        :return: returns true if anywhere in this node's tree the search text appears
        """
        # print("search text: ", search_text)
        if self.node.text is None:
            return False
        return search_text in self.node.text.strip()
