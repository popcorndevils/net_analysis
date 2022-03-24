from ._g_element import GElement

class GNode(GElement):
    def __init__(self, n, parent = None):
        super().__init__(parent)
        self.n = n

    def __str__(self):
        return str(self.n)
