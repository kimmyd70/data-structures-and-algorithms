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


    def zip_lists(list1,list2):
        error = 'Cannot zip two empty lists'
        if list1:
            head1 = list1.head
            
        elif list2:
            head2 = list2.head
        else:
            return error

        store_next = head2.next
        length1 = len(list1)
        length2 = len(list2)
        
        # happy path with lists the same length
        
        while head1:
            if not head1 or not head2:
                head2.next = head1.next
                head1.next = head2
                return list1
            else:
                store_next = store_next.next
                head2.next = head1.next
                head1.next = head2
                
                head1 = head1.next.next
                head2 = head2.next
                
        return list1
    
