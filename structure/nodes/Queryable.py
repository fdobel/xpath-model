from abc import abstractmethod, ABCMeta
from types import GeneratorType
from .XPathResult import XPathResult


class Queryable:
    @abstractmethod
    def iter(self) -> GeneratorType:
        pass

    @abstractmethod
    def query_node(self):
        pass


class XPathQueryable(Queryable):

    @abstractmethod
    def xpath(self, query) -> XPathResult:
        raise RuntimeError("Abstract")

    def select_all_nodes(self, node_name) -> XPathResult:
        return self.xpath(".//%s" % node_name)

    def select_all_nodes_with_class(self, node_name, class_name) -> XPathResult:
        return self.xpath('.//%s[contains(@class,"%s")]' % (node_name, class_name))

    def contains_link_with(self, link):
        if self.href is None:
            return False
        return link in self.href
    """
    def nodes_with_text(self, search_text):

        for node in self.iter():
            if node.text is not None and search_text in node.text:
                yield node
    """
    #def contains_text(self, search_text):
    #    """
    #
    #    :param search_text:
    #    :return: returns true if anywhere in this node's tree the search text appears
    #    """
    #    return search_text in self.concat_texts()


