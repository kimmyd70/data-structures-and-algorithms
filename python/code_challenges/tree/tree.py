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
    
    # def add (self,insert_value):
    #     """ takes in the value to add NOTE: all BST methods assume use of an ordered tree """
    #     if not self:
    #         raise InvalidOperationError('something went wrong with creating a tree')
    #         return
    #     if not self.root:
    #         raise InvalidOperationError('your tree is empty; value added at the root')
    #         self.root = Node(insert_value)
    #         return
        

    #     if position == 'left':
    #         right = None
    #         left = value
    #     elif position == 'right':
    #         left = None
    #         right = value
        
    #     new_sub_tree = BinarySearchTree(Node(root, left, right))
    #     return new_sub_tree
        pass

        
    def contains(self, search_value):
        """ takes in the value to be searched; returns boolean """
        if not self:
            raise InvalidOperationError('something went wrong with creating a tree')
            return
        if not self.root:
            raise InvalidOperationError('your tree is empty')
            return
        def traverse(root, search_value):
            """ recursive traverse updating root until search_value is found """      
            # BST has less than on left and greater on right of current root
            if root:     
                if root.value == search_value:
                    return True
                if search_value < root.value:
                    return traverse(root.left, search_value)
                    # skips to recursion to check this root and traverse left 
                    # subtree at each subsequent root
            
                if search_value > root.value:
                    return traverse(root.right, search_value)
                    # skips to recursion to check this root and traverse right
                    # subtree at each subsequent root
            #exits if there are no subtrees past this
            return False
        # recursion until search_value found or all subtrees exhausted
        return traverse(self.root, search_value)
    
    
