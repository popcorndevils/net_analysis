from ._g_edge import GEdge

class GEdgesHandler:
    def __init__(self, g):
        self._g = g

    def get_attributes(self, edge = None):
        return {k: v for k, v in self._g.edges[edge.n1, edge.n2].items() if k != "events"}

    def get_events(self, edge):
        if isinstance(edge, GEdge):
            return self._g.edges[edge.n1, edge.n2]["events"]
        return self._g.edges[edge]["events"]

    def __iter__(self):
        for n in self._g.edges:
            yield GEdge(n[0], n[1], self)

    def __getitem__(self, *args):
        if len(args) == 1:
            _k = args[0]
            if isinstance(_k, GEdge):
                return self.get_attributes(_k)
            else:
                return self._g.edges[_k]
