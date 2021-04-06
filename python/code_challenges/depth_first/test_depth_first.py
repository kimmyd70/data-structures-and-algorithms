import pytest
from depth_first import Graph, Vertex, Edge

# g = Graph()
# g.addEdge(0, 1)
# g.addEdge(0, 2)
# g.addEdge(1, 2)
# g.addEdge(2, 0)
# g.addEdge(2, 3)
# g.addEdge(3, 3)

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
    first_edge = graph.add_edge(a,a,6)

    actual = graph.depth_first(a)
    expected = 'nodes in order [a]'
    assert actual == expected