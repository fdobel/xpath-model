
class NodeValue:

    def __init__(self, tag, attrib, text):
        self.tag = tag
        self.attrib = attrib
        self.text = text

        self.class_attrib = ''
        self.href = None

        if 'class' in self.attrib:
            self.class_attrib = self.attrib['class']
        if 'href' in self.attrib:
            self.href = self.attrib['href']

    def __eq__(self, other):
        return self.tag == other.tag and \
               self.class_attrib == other.class_attrib and \
               self.href == other.href

    def __str__(self):
        return "%s[%s]" % (self.tag, self.class_attrib)

