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
            # head2 = list2.head
        elif list2:
            head1 = list2.head
            # head2 = list1.head
        else:
            return error

        
        length1 = len(list1)
        length2 = len(list2)
        
        # happy path with lists the same length
        
        while list1 or list2:
            if length1 == length2:
                for item in range(0,length1):
                    list1.insert_after(list1[item].value,list2[item].value)        
            return head1

    
    # whiteboard flow
    
#     define a function with 2 args (LL1, LL2)
# --- set head to LL1 head (assuming not None)
# --- set head to LL2head (if LL1 is None)
# -- throw error when given 2 empty lists
# -- while LL1 or LL2 (is not None)

# --- check lists and compare lengths
# --- take care of case where one list reaches None: pivot to "append the rest of the other list"
# --- insert LL2 node after LL1 current node
# --- return LL1 head pointer


# Edge: 2 empty lists -- will fall out of while loops and print an error


# ** uses insert_after method already written