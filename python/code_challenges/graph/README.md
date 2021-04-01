# Graph Implementation

Developer: Kim Damalas

## PR for this file: https://github.com/kimmyd70/data-structures-and-algorithms/pull/68

This is code challenge 35 of 401-Python (seattle-py-401n2)

Date: 30 March 2021
____________________
### Challenge 

Implement your own Graph. The graph should be represented as an adjacency list, and should include the following methods:

1.  AddNode()
    - Adds a new node to the graph
    - Takes in the value of that node
    - Returns the added node
2.  AddEdge()
    - Adds a new edge between two nodes in the graph
    - Include the ability to have a “weight”
    - Takes in the two nodes to be connected by the edge
        - Both nodes should already be in the Graph
3. GetNodes()
    - Returns all of the nodes in the graph as a collection (set, list, or similar)
4. GetNeighbors()
    - Returns a collection of edges connected to the given node
    - Takes in a given node
    - Include the weight of the connection in the returned collection
5. Size()
    - Returns the total number of nodes in the graph

____________

## Approach & Efficiency

Approach is using Nodes, Classes


Time:   O(n) -- traverse the entire graph 

Space:  O(n) -- store the entire graph

_____________
## Required Testing

Write unit test to capture:
1. Node can be successfully added to the graph
2. An edge can be successfully added to the graph
3. A collection of all nodes can be properly retrieved from the graph
4. All appropriate neighbors can be retrieved from the graph
5. Neighbors are returned with the weight between nodes included
6. The proper size is returned, representing the number of nodes in the graph
7. A graph with only one node and edge can be properly returned
8. An empty graph properly returns null
_________________

## Whiteboard

CC#35 -- no whiteboard for implementation

