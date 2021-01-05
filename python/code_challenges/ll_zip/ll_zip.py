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
