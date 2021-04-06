import pytest
from depth_first import Graph, Vertex, Edge


# passes
def test_empty_graph():
    g = Graph()
    actual = len(g._adjacency_list)
    expected = 0
    assert actual == expected

# passes    
def test_empty_traverse():
    g = Graph()
    actual = g.depth_first(0)
    expected = 'your graph is empty'
    assert actual == expected
    
#    
def test_one_node():
    graph = Graph()
    a = graph.add_node('a')
    graph.add_edge(a,a)

    actual = graph.depth_first(a)
    expected = 'nodes in order [a]'
    assert actual == expected
    
#    
def test_small_graph():
    g = Graph()
    a = g.add_node(0)
    b = g.add_node(1)
    c = g.add_node (2)
    d = g.add_node (3)
    g.add_edge(a, b)
    g.add_edge(a, c)
    g.add_edge(b, c)
    g.add_edge(c, a)
    g.add_edge(c, d)
    g.add_edge(d, a)

    actual = g.depth_first(a)
    expected = 'nodes in order [0,1,2,3]'
    assert actual == expected
