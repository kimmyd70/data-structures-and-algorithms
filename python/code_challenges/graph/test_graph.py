import pytest
from graph import Vertex, Graph
# from testfixtures import should_raise

# passes
def test_add_node():
    graph = Graph()
    expected = 'a'
    actual = graph.add_node('a').value
    assert expected == actual

# passes
def test_add_vertex_pass():
    vertex = Vertex('a')
    actual = vertex.value
    expected = 'a'
    assert actual == expected

# passes
def test_add_vertex_fail():
    vertex = Vertex('a')
    actual = vertex.value
    expected = 'b'
    assert actual != expected

    
# passes
def test_add_edge_true():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    graph.add_edge(a, b)
    assert True
    

# @pytest.mark.skip('Pending')
def test_get_collection():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    c = graph.add_node('c')
    
    first_edge = graph.add_edge(a,b,6)
    second_edge = graph.add_edge(b,c,2)
    third_edge = graph.add_edge(c,a)
    
    actual = graph.get_node()
    expected = [a,b,c]
    assert actual == expected

# passes
def test_get_neighbor_count():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    c = graph.add_node('c')
    
    first_edge = graph.add_edge(a,b,6)
    second_edge = graph.add_edge(b,c,2)
    third_edge = graph.add_edge(c,a)

    actual = graph.get_neighbor(a)
    expected = [first_edge]
    assert actual == expected
    
    
# passes
def test_get_neighbor_count_fail():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    c = graph.add_node('c')
    
    first_edge = graph.add_edge(a,b,6)
    second_edge = graph.add_edge(b,c,2)
    third_edge = graph.add_edge(c,a)

    actual = graph.get_neighbor(a)
    expected = [first_edge, second_edge]
    assert actual != expected

# passes
def test_one_node():
    graph = Graph()
    a = graph.add_node('a')
    
    first_edge = graph.add_edge(a,a,6)

    actual = graph.get_neighbor(a)
    expected = [first_edge]
    assert actual == expected
    

# passes
def test_size():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    expected = 2
    actual = graph.size()
    assert actual == expected
    
# passes
def test_size_fail():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    expected = 3
    actual = graph.size()
    assert actual != expected
    

# passes -- this was new to me!
def test_size_empty():
    with pytest.raises(ValueError) as e_info:
        graph = Graph()
        graph.size()