

class Sequence:

    def __init__(self, sequence, elements_equal=lambda a, b: a == b):
        self.sequence = sequence
        self._elements_equal = elements_equal

    def subsequence(self, end_idx, start_idx=0):
        return Sequence(self.sequence[start_idx:end_idx])

    def __eq__(self, other):
        # print(self.sequence, other.sequence)
        return all([self._elements_equal(a, b) for a, b in zip(self.sequence, other.sequence)])

    def __iter__(self):
        for a in self.sequence:
            yield a

    def __str__(self):
        return str(self.sequence)

    def match_longest_start_sequence(self, sequence2: 'Sequence', key=lambda x: x):
        i = 0

        for element1, element2 in self.iterate_sequences(self, sequence2, key):
            if element1 != element2:
                break
            i += 1

        return self.subsequence(i)

    def compare(self, other, key=lambda x: x):
        return all([a == b for a, b in self.iterate_sequences(self, other, key)])

    @classmethod
    def iterate_sequences(cls, s1, s2, key=lambda x: x):
        return zip(map(key, s1.sequence), map(key, s2.sequence))


def match_longest_start_sequences(sequences, key=lambda x: x):

    i = 0
    current = sequences[0]
    for next_sequence in sequences[1:]:
        current = current.match_longest_start_sequence(next_sequence, key)
    return current