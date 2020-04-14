from .Node import XPathNode


class Position:

    @classmethod
    def is_descendant_of(cls, node: XPathNode, other_node):
        for ancestor in cls.ancestors(node).nodes():
            if ancestor == other_node:
                return True
        return False

    @classmethod
    def ancestors(cls, node) -> 'Position':
        return Position(node)

    def __init__(self, node, class_=None):

        self.ancestors = list(reversed([a for a in node.iterancestors()]))
        # print(self.tags())

    def tags(self):
        return list(map(lambda a: a.tag, self.ancestors))

    def nodes(self):
        return list(map(lambda a: XPathNode(a), self.ancestors))

    def __str__(self):
        ancestor_tags = self.tags()
        duplicity_tags = ["%s-%s" % (len([_ for _ in group]), group_name) for [group_name, group] in groupby(ancestor_tags)]

        return "%s" % '/'.join(duplicity_tags)

    def __iter__(self):
        return self.ancestors.__iter__()

    #def difference(self, child_position):
    #    return str(child_position) + " --- " + str(self) + " +++ " + str(child_position.match(self)) + "\n"  # todo

    """def match(self, match_position):
        sm = SequenceMatcher()

        # print(self.tags(), match_position.tags())

        sm.set_seq1(self.tags())
        sm.set_seq2(match_position.tags())

        return sm.ratio()"""