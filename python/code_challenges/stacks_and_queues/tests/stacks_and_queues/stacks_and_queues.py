class Node():
    def __init__(self, value, next = None):
        self.value = value
        self.next = next
        
class Stack():
    def __init__(self, node = None):
        self.top = node
        
    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node
        
    def pop (self):
        if self.is_empty():
            raise ("Not allowed on empty structure")
        node = self.top.next
        return node.value
    
    def peek (self):
        if self.is_empty():
            raise ("Not allowed on empty structure")
        return self.top.value
    def is_empty(self):
        return True
    
    class Queue():
        def __init__(self):
            self.front = None
            self.rear = None