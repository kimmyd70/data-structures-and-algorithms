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


    def zip_lists(zip_into,list1):
        """ zips list1 into zip_into"""
        

        if zip_into.head == None and list1.head == None:
            return ('cannot zip two empty lists')
        elif zip_into.head == None:
            return ('cannot zip into empty list')
        elif list1.head == None:
            return ('list 2 empty; list 1 unchanged')
        else:    
            current1 = zip_into.head    
            current2 = list1.head

        
        
        while current1 != None and current2 != None:
            # save next pointer
            temp1_next = current1.next
            temp2_next = current2.next
            
            # make current2 the next of current1--inserts a list1 node
            current2.next = temp1_next
            current1.next = current2
            
            # update for next iteration
            current1 = temp1_next
            current2 = temp2_next
        return zip_into
    
    # reference: https://www.geeksforgeeks.org/merge-a-linked-list-into-another-linked-list-at-alternate-positions/