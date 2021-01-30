


class Node:
    def __init__ (self, value = None, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
        raise('something went wrong with Node instantiation')
        
class BinaryTree:
    def __init__(self, root = None):
        self.root = root
        
    def __str__(self):
        output_left = ''
        output_right = ''
        current = self.root
        while current:
            output_left += f'{{ {current.value} }} -> '
            current = current.left
            
        current = self.root
        
        while current:
            output_right += f'{{ {current.value} }} -> '
            current = current.right
        return f'left: {output_left} and right: {output_right}'
        
        
    def pre_order():
        #raise('something went wrong with pre_order operation')
        pass
    
    def in_order():
        #raise('something went wrong with in_order operation')
        pass

    def post_order():
        #raise('something went wrong with post_order operation')
        pass
        
class BinarySearchTree(BinaryTree):
    def __init__():
        # BinaryTree()
        pass

    def add():
        #raise('something went wrong with add operation')
        pass
    
    def contains():
        #raise('something went wrong with contains operation')
        pass
    