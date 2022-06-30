from collections import OrderedDict

MEMORY_MAX_SIZE = 6


class LimitedSizeDict(OrderedDict):
    def __init__(self, *args, **kwds):
        self.size_limit = MEMORY_MAX_SIZE
        OrderedDict.__init__(self, *args, **kwds)
        self._check_size_limit()

    def __setitem__(self, key, value):
        OrderedDict.__setitem__(self, key, value)
        self._check_size_limit()

    def _check_size_limit(self):
        if self.size_limit is not None:
            while len(self) > self.size_limit:
                self.popitem(last=False)


class LookUpMemory:
    def __init__(self):
        self.memory = LimitedSizeDict()

    def contains(self, location):
        return location in self.memory

    def put(self, location, cell):
        self.memory[location] = cell
