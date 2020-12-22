class Node:
    """
    Put docstring here
    """

    def __init__(self,value,next=None):
        # initialization here
        self.value = value
        self.next = next
        
    def __str__():
        #returns string "{ a } -> { b } -> { c } -> NULL"
        pass

class LinkedList:
    """ doc """
    
    def __init__(self, head=None):
        self.head = head
    
    def insert(self, value):
        node = Node(value) # value 8 next None

        if self.head is not None:
            node.next = self.head
        self.head = node
    
    def includes(self,inc_value):
        current = self.head
        
        while current is not None:
            if current.value == inc_value:
                return True
        current = current.next
        
        return False
    
# create Linked List  
if __name__ == "__main__":
    new_node = Node(1)
    new_linked = LinkedList()
    print (new_linked)
    
    new_linked_1 = LinkedList(new_node)