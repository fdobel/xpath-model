from typing import List
from .xpath import XPath

from structure.nodes.Node import XPathNode
from structure.nodes.NodeSet import NodeSet


class ExtractedDescriptors:

    def __init__(self, name, extraction: List[XPathNode], description, node_sets: List[NodeSet]):
        self.name = name
        self.extraction = extraction
        self.description = description
        self.__node_sets = node_sets

    @property
    def extracted_node(self) -> XPathNode:
        return self.extraction[len(self.extraction) - 1]

    def describe(self):
        s = "<%s  desc=%s value=%s>" % (self.name, self.description, str(self.extracted_node.value))
        return s

    def to_xpath(self):
        return XPath(self.extraction).with_classes()

    def extracted_from(self):
        return self.__node_sets

    def __str__(self):
        return self.describe()
