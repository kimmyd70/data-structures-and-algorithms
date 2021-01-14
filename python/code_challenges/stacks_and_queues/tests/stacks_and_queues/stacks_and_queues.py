
class InvalidOperationError(BaseException):
    pass
    
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
            raise InvalidOperationError("Not allowed on empty structure")
        node = self.top
        self.top = self.top.next
        return node.value
    
    def peek (self):
        if self.is_empty():
            raise InvalidOperationError("Not allowed on empty structure")
        return self.top.value
    
    def is_empty(self):
        
        return self.top == None
    
class Queue():
    def __init__(self):
        self.front = None
        self.rear = None