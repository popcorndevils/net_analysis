import inspect

class GrapherAttribute:
    def __init__(self, name, function, *args, **kwargs):
        self._name = name
        self._function = function
        self._args = args
        self._kwargs = kwargs
        self._params = [
            _s.replace(" ", "").split("=")[0]
            for _s in str(inspect.signature(self.function))[1:-1].split(", ")
        ]

        self._check_args(function, *args, **kwargs)

    def apply(self, graph, node = None, edge = None):
        _pos_params = [p for p in self.args]
        _kw_params = {k: v for k, v in self.kwargs.items()}
        _args = []

        for _p in self._params:
            if _p == "node" and node is not None:
                _args.append(node)
            elif _p == "edge" and edge is not None:
                _args.append(edge)
            elif _p == "graph":
                _args.append(graph)
            elif _p not in self.kwargs and len(_pos_params) > 0:
                _args.append(_pos_params.pop(0))
            else:
                _args.append(_kw_params.pop(_p))

        assert len(_pos_params) == 0
        assert len(_kw_params) == 0

        return self.function(*_args)

        # # _n_kwargs = 0
        # # if function.__defaults__ is not None:
        # #     _n_kwargs = len(function.__defaults__)
        # # _n_pargs = function.__code__.co_argcount - _n_kwargs

        # if "node" in _sig_args or "edge" in _sig_args:
        #     _args.append(node_or_edge)
        # if "graph" in _sig_args:
        #     _args.append(graph)

    # ACCESS
    @property
    def name(self):
        return self._name
    @property
    def function(self):
        return self._function
    @property
    def args(self):
        return self._args
    @property
    def kwargs(self):
        return self._kwargs

    # methods
    def _as_dict(self):
        return {
            "name": self._name,
            "function": self._function,
            "args": self._args,
            "kwargs": self._kwargs,
        }

    def _check_args(self, function, *args, **kwargs):
        _user_args = [p for p in self._params if p not in ["node", "edge", "graph"]]
        assert len(_user_args) == len(args) + len(kwargs)
