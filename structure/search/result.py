from functools import reduce


class _AbstractResult:

    #def flat_map(self):  # todo why zero index
    #    return map(lambda x: x[0] if len(x) > 0 else None, self.result)

    def __init__(self, query, result):
        self.query = query
        self.result = result

    def __len__(self):
        return len(self.result)

    def __str__(self):
        return "<QueryResult #results:%d results:%s >" % (
            len(self.result), ','.join(map(lambda x: str(x.value), self.result))
        )


class QueryResult(_AbstractResult):

    def __getitem__(self, idx):
        return self.result[idx]


class MultiQueryResult(_AbstractResult):

    def __str__(self):
        return "<MultiQueryResult #results:%d results:%s >" % (len(self.result),
                                        ','.join(map(lambda x: str(x), self.result)))

    def output_format(self, func=lambda x: x):
        return list(map(func, self.result))
