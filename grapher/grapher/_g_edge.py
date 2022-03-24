from ._g_element import GElement

class GEdge(GElement):
    def __init__(self, n1, n2, parent = None):
        super().__init__(parent)
        self.n1 = n1
        self.n2 = n2

    def __str__(self):
        return str((self.n1, self.n2))
