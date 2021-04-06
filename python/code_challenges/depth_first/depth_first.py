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
    
    
    def depth_first(self,v):
        if self._adjacency_list == {}:
            return 'your graph is empty'
        
        if v not in self._adjacency_list:
            return "that vertex isn't in your graph"
        
        visited = []
        
        # v is starting vertex 
        # v = self._adjacency_list[0]

        def traverse(v):
            nonlocal visited
            visited.append(v)
            for neighbor in self._adjacency_list[v]:
                if neighbor not in visited:
                    traverse(neighbor)

        return (f'nodes in order {visited}')
    
    
class Vertex:
    def __init__(self, value):
        self.value = value

class Edge:
    def __init__(self, vertex, weight=1):
        self.vertex = vertex
        self.weight = weight