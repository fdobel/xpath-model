

# todo wrong file?
from query.matching.sequence import Sequence, match_longest_start_sequences
from structure.nodes.Position import Position


class NodeSet:

    def __init__(self, nodes):
        """

        :param nodes: array of Node instances
        """
        self.nodes = nodes

    def common_ancestor(self):
        """

        :return: Sequence object
        """

        if len(self.nodes) == 0:
            raise AttributeError

        sequences = [Sequence(Position(node).nodes()) for node in self.nodes]
        return match_longest_start_sequences(sequences, lambda node: node.node)

    def __iter__(self):
        for node in self.nodes:
            yield node

    def __str__(self):
        return "<NodeSet %s>" % ", ".join(map(lambda x: x.value.__str__(), self.nodes))