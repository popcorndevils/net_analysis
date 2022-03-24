import networkx as nx
import pandas as pd

from ._grapher_attribute import GrapherAttribute
from ._g_node import GNode
from ._g_edge import GEdge
from ._g_nodes_handler import GNodesHandler
from ._g_edges_handler import GEdgesHandler

class Grapher:
    def __init__(self, data: pd.DataFrame, n1: str, n2: str):
        self._n1 = n1
        self._g = nx.Graph()
        _packets = data.apply(Grapher.extract_packet, axis = 1, fields = data.columns)

        for p in _packets:
            _n1 = p[n1.lower()]
            _n2 = p[n2.lower()]
            if not self._g.has_edge(_n1, _n2):
                self._g.add_edge(_n1, _n2, events = [])

            _e = self._g[_n1][_n2]
            _e["events"].append({k: v for k, v in p.items()})

    @property
    def edges(self):
        return GEdgesHandler(self._g)
    @property
    def nodes(self):
        return GNodesHandler(self._g)

    def apply(self, *args, feature = "node"):
        _attr_list = None
        if len(args) > 0:
            if isinstance(args[0], GrapherAttribute):
                _attr_list = args
            elif isinstance(args[0], list) and len(args[0]) > 0 and isinstance(args[0][0], GrapherAttribute):
                _attr_list = args[0]

        if _attr_list is None:
            raise ValueError("No attributes were found.")

        if feature == "node":
            self._apply_node(_attr_list)
        elif feature == "edge":
            self._apply_edge(_attr_list)
        else:
            raise ValueError("feature only accepts \"node\" or \"edge\"")

    # HELPERS
    def _apply_node(self, attributes):
        _attrib = {
            n.n: {
                a.name: a.apply(self, node = n)
                for a in attributes
            }
            for n in self.nodes
        }
        nx.set_node_attributes(self._g, _attrib)

    def _apply_edge(self, attributes):
        _attrib = {
            (e.n1, e.n2): {
                a.name: a.apply(self, edge = e)
                for a in attributes
            }
            for e in self.edges
        }
        nx.set_edge_attributes(self._g, _attrib)

    # SPECIALS
    def __getitem__(self, *args):
        if len(args) == 1:
            _k = args[0]
            if isinstance(_k, GNode):
                return [GNode(n) for n in self._g[_k.n]]
            elif isinstance(_k, GEdge):
                return self.get_edge_attributes(_k)

    # STATIC METHODS
    @staticmethod
    def extract_packet(row, fields: list[str]):
        _output = {}
        for f in fields:
            _output[f.lower()] = row[f]
        return _output
