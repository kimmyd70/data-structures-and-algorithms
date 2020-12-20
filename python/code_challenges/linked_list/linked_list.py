class Node:
    """
    Put docstring here
    """

    def __init__(self,value=0,next=None):
        # initialization here
        self.value = value
        self.next = next
        

    def some_method(self):
        # method body here
        pass
class LinkedList:
    """ doc """
    
    def __init__(self, head, values=None):
        self.head = head
    
    def insert(self, value):
        node = Node(value) # value 8 next None

        if self.head is not None:
            node.next = self.head
        self.head = node
    
    def includes(inc_value):
        #returns boolean if/if not inc_value in list
        pass
    
    def __str__():
        #returns string "{ a } -> { b } -> { c } -> NULL"
        pass
    
