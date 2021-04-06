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
    graph.add_node('a')
    graph.add_edge('a','a')

    actual = graph.depth_first(a)
    expected = 'nodes in order [a]'
    assert actual == expected
    
#    
def test_small_graph():
    g = Graph()
    g.add_node(0)
    g.add_node(1)
    g.add_node (2)
    g.add_node (3)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    actual = graph.depth_first(0)
    expected = 'nodes in order [0,1,2,3]'
    assert actual == expected
