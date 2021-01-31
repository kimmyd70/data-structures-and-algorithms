class InvalidOperationError(BaseException):
    pass


class Node:
    def __init__ (self, value = None, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
        
class BinaryTree:
    def __init__(self, root = None):
        self.root = root

        
    def __str__(self):
        """ function used to test instantiation of one-node BT and BST"""
        # baby steps (TDD)

        output_left = []
        output_right = []
        current = self.root
        while current:
            output_left.append(current.value)
            current = current.left
            
        current = self.root
        
        while current:
            output_right.append(current.value)
            current = current.right
        return f'left: {output_left} and right: {output_right}'
        
        
    def pre_order(self, root = None):
        """ function prints root then left traverse """
        if not self:
            raise InvalidOperationError('something went wrong with creating a tree')
            return
        if not root:
            raise InvalidOperationError('your tree is empty')
            return
        
        def traverse(root):
            print(root.value)
            if root.left:
                traverse(root.left)
            
            if root.right:
                traverse(root.right)
        traverse(self.root)

        pass
    
    def in_order(self, root = None):
        """ function left traverse then prints root  """
        
        if not self:
            raise InvalidOperationError('something went wrong with creating a tree')
            return
        if not root:
            raise InvalidOperationError('your tree is empty')
            return
        
        def traverse(root):
            if root.left:
                traverse(root.left)
            print(root.value)
            
            if root.right:
                traverse(root.right)
        traverse(self.root)
        # pass

    def post_order(self, root = None):
        if not self:
            raise InvalidOperationError('something went wrong with creating a tree')
            return
        if not root:
            raise InvalidOperationError('your tree is empty')
            return
        
class BinarySearchTree(BinaryTree):
    def __init__(self, root = None):
        self.root = root
        
    def add(self, value):
        # if not self:
        #     raise InvalidOperationError('something went wrong with add operation')
        pass
    
    def contains(self,value):
        # if not self:
        #     raise InvalidOperationError('something went wrong with post_order operation')
        pass
    