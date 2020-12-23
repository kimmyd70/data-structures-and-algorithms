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
    
    
# append(value): insert value at end of list
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
    
# insert_before(value, newVal): insert newVal before 
# first instance of value 
    def insert_before(self, value, newVal):
        new_node = Node(newVal)
        current = self.head
        
        # checking for empty list and puts at the head
        if current is None:
            self.insert(new_node)
            return
        # inserts after a node matching our search value
        while current.next is not None:
            if current.next.value == value:
                new_node.next = current.next
                current.next = new_node
            current = current.next    
            return
        
# insert_after(value, newVal): insert newVal after
# first instance of value 

######### why does it fail when trying to insert at the end? ########

    def insert_after(self, value, newVal):
        new_node = Node(newVal)
        current = self.head
        
        # checking for empty list and puts at the head
        if current is None:
            self.insert(new_node)
            return
        
        # inserts after a node matching our search value
        while current is not None:
            current = current.next    
            if current.value == value:
                new_node.next = current.next
                current.next = new_node
            return

# function to clear the list
    def clear_list(self):
        pass

    
# create Linked List  
    def insert_many(self):
        node = Node(0)
        new_list = LinkedList(node)
        list_length = 0
        
        for value in range(1,5):
            new_list.insert(value)
            list_length += 1
        
        return new_list

        # pass
        # new_linked = []
        # for value in range(1,5):
            # current = self.head
            # self.insert(value)
            # new_linked.append(current.value)
            # current = current.next
        # return



