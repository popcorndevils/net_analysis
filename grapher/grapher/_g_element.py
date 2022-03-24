class GElement:
    def __init__(self, parent):
        self._parent = parent

    def __getitem__(self, *args):
        if len(args) == 1 and self._parent is not None:
            return self.parent[args[0]]
