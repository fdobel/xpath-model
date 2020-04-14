from abc import abstractmethod


class XPathResult:

    def __init__(self, xpath_result):
        self.xpath_result = xpath_result

    @abstractmethod
    def __iter__(self):
        raise RuntimeError("abstract method")