
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
        
    def q_is_empty(self):
        return self.front == None

        
    def enqueue(self, value = None):
        node = Node(value)
        if self.q_is_empty():
            # assign new node to both front and back if empty Q
            self.front = node
            self.rear = node
        else:    
            self.rear.next = node
            self.rear = node
        
    def dequeue(self, value = None):
        if self.q_is_empty():
            raise InvalidOperationError("Not allowed on empty structure")
        node = self.front
        self.front = self.front.next
        return node.value

    def q_peek(self):
        if self.q_is_empty():
            raise InvalidOperationError("Not allowed on empty structure")
        return self.front.value
