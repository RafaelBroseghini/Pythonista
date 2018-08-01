class OrderedMap(dict):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __iter__(self):
        return iter(sorted(super().__iter__()))


class OrderedSet(set):

    def __init__(self, lst=[]):
        super().__init__(lst)

    def __iter__(self):
        return iter(sorted(super().__iter__()))


class OrderedFrozenSet(frozenset):

    def __init__(self, lst=[]):
        self = frozenset(lst)

    def __iter__(self):
        return iter(sorted(super().__iter__()))
