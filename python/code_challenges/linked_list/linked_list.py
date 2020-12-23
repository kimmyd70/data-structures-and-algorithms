class Node:
    """
    Methods instantiate a node and
    Returns:
        string: { a } -> { b } -> { c } -> NULL
    """

    def __init__(self,value,next = None):
        # initialization here
        self.value = value
        self.next = next
        

class LinkedList:
    """ 
    Methods instantiate a linked list, insert a value, and
    checks for value in the list
    """
    
    def __init__(self, head=None):
        self.head = head
    
    def __str__(self):
        output = ''
        current = self.head
        while current is not None:
            output += f'{{ {current.value} }} -> '
            current = current.next
        return output + 'NULL'
    
    def insert(self, value):
        node = Node(value) 

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
    
    
    def append(self,value):
        new_node = Node(value)
        current = self.head
        # checking for empty list
        if current is None:
            current = new_node
            return
        while current.next is not None:
            current = current.next
            
        current.next = new_node
        return 
    
    def insert_before(self, value, new_value):
        new_node = Node(new_value)
        current = self.head
        
        # checking for empty list
        if current is None:
            self.insert(new_node)
            return
        while current.next is not None:
            if current.next.value == value:
                new_node.next = current.next
                current.next = new_node
            current = current.next    
            return
        

    
# create Linked List  
    def insert_many(self):
        new_linked = []
        current = self.head
        for value in range(1,5):
            self.insert(value)
            new_linked.append(current.value)
            current = current.next

        return(new_linked)
    
# append(value): insert value at end of list

# insert_before(value, newVal): insert newVal before 
# first instance of value 

# insert_after(value, newVal): insert newVal after
# first instance of value 

