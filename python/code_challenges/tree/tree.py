class InvalidOperationError(BaseException):
    pass

class Node:
    """ points to next Node on both side--similar to LL"""
    def __init__ (self, value = None, left = None, right = None):
        """ takes in up to 3 values creating Nodes with each value"""
        self.value = value
        self.left = left
        self.right = right
        
class BinaryTree:
    def __init__(self, root = None):
        self.root = root
        
    # def __str__(self):
    #     if not self:
    #         raise InvalidOperationError('something went wrong with creating a tree')
    #         return

    #     return str(f'root:{self.root}, left:{self.left.value}, right:{self.right.value}')
    
    
    # def add (root, position:str, value):
    #     """ takes in the root value to add node to, the position of new node,
    #     and new node value """
    #     if not root:
    #         raise InvalidOperationError('your tree is empty')
    #         return
    #     if position == 'left':
    #         right = None
    #         left = value
    #     elif position == 'right':
    #         left = None
    #         right = value
        
    #     new_sub_tree = BinaryTree(root, left, right)
    #     return new_sub_tree
            
        
        
    def pre_order(self, root = None):
        """ function prints root then left traverse """
        collection = []
        if not self:
            raise InvalidOperationError('something went wrong with creating a tree')
            return
        if not root:
            raise InvalidOperationError('your tree is empty')
            return
        
        def traverse(root):
            collection.append(root.value)
            # return(root.value)
            if root.left:
                traverse(root.left)
            
            if root.right:
                traverse(root.right)
        traverse(self.root)
        return collection
        
    
    def in_order(self, root = None):
        """ function left traverse then prints root  """
        collection = []

        
        if not self:
            raise InvalidOperationError('something went wrong with creating a tree')
            return
        if not root:
            raise InvalidOperationError('your tree is empty')
            return
        
        def traverse(root):
            if root.left:
                traverse(root.left)
            collection.append(root.value)

            # return(root.value)
            
            if root.right:
                traverse(root.right)
        traverse(self.root)
        
        return collection
        

    def post_order(self, root = None):
        """ function does left traverse, right traverse, then print root """

        collection = []
        
        if not self:
            raise InvalidOperationError('something went wrong with creating a tree')
            return
        if not root:
            raise InvalidOperationError('your tree is empty')
            return
        
        def traverse(root):
            if root.left:
                traverse(root.left)
            
            if root.right:
                traverse(root.right)
            collection.append(root.value)
    
            # return(root.value)
        traverse(self.root)
        
        return collection

        
class BinarySearchTree(BinaryTree):
    def __init__(self, root = None, left = None, right = None):
        self.root = root
        
        
    # def __str__(self):
    #     return str(f'root:{self.root}, left:{self.left}, right:{self.right}')
    
    def add (self, root, position:str, value):
        """ takes in the root value to add node to, the position of new node,
        and new node value """
        # if not self:
        #     raise InvalidOperationError('something went wrong with creating a tree')
        #     return
        # if not root:
        #     raise InvalidOperationError('your tree is empty')
        #     return

        # if position == 'left':
        #     right = None
        #     left = value
        # elif position == 'right':
        #     left = None
        #     right = value
        
        # new_sub_tree = BinarySearchTree(Node(root, left, right))
        # return new_sub_tree
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
    
    def contains(self,value,method):
        """ takes in the value to be searched and search method string """
        if not self:
            raise InvalidOperationError('something went wrong with creating a tree')
            return
        if not self.root:
            raise InvalidOperationError('your tree is empty')
            return
        # first root is not a node
        new_root = Node(self.root)
        if new_root.value == value:
            return True
        else:      
            while new_root.value:
                if new_root.value == value:
                    return True
                #dynamic assignment of method used
                if method == 'pre_order':
                    self.pre_order(new_root)
                elif method == 'post_order':
                    self.post_order(new_root)
                elif method == 'in_order':
                    self.in_order(new_root)
                else:
                    raise InvalidOperationError('try again with pre_order, in_order, or post_order argument for method')
        return False
        # pass
    
    
