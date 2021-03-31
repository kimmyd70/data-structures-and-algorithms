
class Graph:

    def __init__(self):
        self._adjacency_list = {}
    
    def add_node(self, value):
        v = Vertex(value)
        self._adjacency_list[v] = []
        return v

    def add_edge(self, start_vertex, end_vertex, weight=1):
        if start_vertex not in self._adjacency_list:
            raise KeyError('Start Vertex not in Graph')
        if end_vertex not in self._adjacency_list:
            raise KeyError('End Vertex not in Graph')
        edge = Edge(end_vertex, weight)
        adjacencies = self._adjacency_list[start_vertex]
        adjacencies.append(edge)
        return edge

    def get_node(self):
        if len(self._adjacency_list) == 0:
            raise ValueError('Graph is Empty')
        
        return list(self._adjacency_list)

    def get_neighbor(self, v):
        # access dictionary for key = v and return adjacency_list[v]
        if v not in self._adjacency_list:
            raise KeyError('Vertex not in Graph')

        return self._adjacency_list[v]

    def size(self):
        if len(self._adjacency_list) == 0:
            raise ValueError('The Graph is Empty')
        return len(self._adjacency_list)


class Vertex:
    def __init__(self, value):
        self.value = value

class Edge:
    def __init__(self, vertex, weight=1):
        self.vertex = vertex
        self.weight = weight