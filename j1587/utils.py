class SparseList(list):
    def __setitem__(self, index, value):
        missing = index - len(self) + 1
        if missing > 0:
            self.extend([None] * missing)
        list.__setitem__(self, index, value)

    def insert(self, index, value):
        self[index] = value
        return self

    def __getitem__(self, index):
        try:
            return list.__getitem__(self, index)
        except IndexError:
            return None


def get_by_id(key, keys, items):
    """
    Creates a dictionary from the results of an index lookup by key on items.
    Provide a list of keys to map to the found item.
    """
    details = items[key]
    if details is None:
        return None
    return dict(
        (keys[i], value) for i, value in enumerate(details) if bool(value))
