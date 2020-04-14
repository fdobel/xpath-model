import lxml.etree as ET
from structure.nodes.Queryable import XPathQueryable
from structure.nodes.Node import XPathNode, NodeXPathResult
from structure.nodes.XPathResult import XPathResult


class XPathEnvironment(XPathQueryable):

    class Builder:

        def __init__(self):
            self.environment = None

        @classmethod
        def environment_from_string(cls, html):
            """
            :param html:
            :return: object for which we can call .xpath function
            """
            html_parser = ET.HTMLParser()
            return ET.fromstring(html, parser=html_parser)

        def from_file(self, file):
            with open(file, 'rb') as f:
                self.set_environment(self.environment_from_string(f.read()))  # read file and pass it to parser.
            return self.finalize()

        def set_environment(self, environment):
            self.environment = environment
            return self

        def finalize(self):
            if self.environment is None:
                raise ValueError("environment not set")
            return XPathEnvironment(self.environment)

    def __init__(self, environment):
        self.environment = environment

    def xpath(self, query) -> XPathResult:
        return NodeXPathResult(self.query_node().xpath(query))

    @classmethod
    def build(cls):
        return XPathEnvironment.Builder()

    def iter(self):
        for a in self.node.iter():
            yield XPathNode(a)

    @property
    def node(self):
        return self.environment

    def query_node(self):
        return self.environment
