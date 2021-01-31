class InvalidOperationError(BaseException):
    pass


class Node:
    def __init__ (self, value = None):
        self.value = value
        
class BinaryTree:
    def __init__(self, root = None, left = None, right = None):
        """ takes in up to 3 values creating Nodes with each value"""
        self.root = Node(root)
        self.left = Node(left)
        self.right = Node(right)
        
    def __str__(self):
        return str(f'root:{self.root.value}, left:{self.left.value}, right:{self.right.value}')
    
    def add_left (root, left = None):
        """ takes in a root and adds value to left; instantiates a sub-tree"""
        right = None
        new_tree_left = BinaryTree(root, left, right)
        return new_tree_left
        
    def add_right (root,right):
        """ takes in a root and adds value to left; instantiates a sub-tree"""
        left = None
        new_tree_right = BinaryTree(root, left, right)
        return new_tree_right

    # def __str__(self):
    #     """ function used to test instantiation of one-node BT and BST"""
    #     # baby steps (TDD)

    #     output_left = []
    #     output_right = []
    #     current = self.root
    #     while current:
    #         output_left.append(current.value)
    #         current = current.left
            
    #     current = self.root
        
    #     while current:
    #         output_right.append(current.value)
    #         current = current.right
    #     return f'left: {output_left} and right: {output_right}'
        
        
    def pre_order(self, root = None):
    #     """ function prints root then left traverse """
    #     collection = []
    #     if not self:
    #         raise InvalidOperationError('something went wrong with creating a tree')
    #         return
    #     if not root:
    #         raise InvalidOperationError('your tree is empty')
    #         return
        
    #     def traverse(root):
    #         collection.append(root)
    #         return(root.value)
    #         if root.left:
    #             traverse(root.left)
            
    #         if root.right:
    #             traverse(root.right)
    #     traverse(self.root)
    #     return collection
        

        pass
    
    def in_order(self, root = None):
        # """ function left traverse then prints root  """
        
        # if not self:
        #     raise InvalidOperationError('something went wrong with creating a tree')
        #     return
        # if not root:
        #     raise InvalidOperationError('your tree is empty')
        #     return
        
        # def traverse(root):
        #     if root.left:
        #         traverse(root.left)
        #     return(root.value)
            
        #     if root.right:
        #         traverse(root.right)
        # traverse(self.root)
        pass

    def post_order(self, root = None):
        """ function does left traverse, right traverse, then print root """

        # if not self:
        #     raise InvalidOperationError('something went wrong with creating a tree')
        #     return
        # if not root:
        #     raise InvalidOperationError('your tree is empty')
        #     return
        
        # def traverse(root):
        #     if root.left:
        #         traverse(root.left)
            
        #     if root.right:
        #         traverse(root.right)
                
        #     return(root.value)
        # traverse(self.root)
        pass

        
class BinarySearchTree(BinaryTree):
    def __init__(self, root = None, left = None, right = None):
        # self.root = root
        # self.left = left
        # self.right = right
        pass
        
    def add(self, value = None, position = None):
        # """ Input = value:str or integer, position:string)
        #     Output = Node at position with .value = value """
        # if not self:
        #     raise InvalidOperationError('something went wrong with creating a tree')
        #     return
        # if not root:
        #     raise InvalidOperationError('your tree is empty')
        #     return
        # new_node = BinarySearchTree(Node(value), position)
        pass
    
    def contains(self,value):
        # if not self:
        #     raise InvalidOperationError('something went wrong with creating a tree')
        #     return
        # if not root:
        #     raise InvalidOperationError('your tree is empty')
        #     return
        pass
    