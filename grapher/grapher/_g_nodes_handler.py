from ._g_node import GNode

class GNodesHandler:
    def __init__(self, g):
        self._g = g

    def __iter__(self):
        for n in self._g.nodes:
            yield GNode(n, self)

    def __getitem__(self, *args):
        if len(args) == 1:
            _k = args[0]
            if isinstance(_k, GNode):
                return self._g.nodes[_k.n]
            else:
                return self._g.nodes[_k]
