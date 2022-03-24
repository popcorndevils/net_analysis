import pytest

def test_import_grapher():
    from grapher import Grapher
    assert Grapher() is not None
    
def test_import_plotter():
    from grapher import Plotter
    assert Plotter is not None