from tree import Node, BinaryTree 
from tree import BinarySearchTree
import pytest


# 15 tests total
# 1. Passes--Can successfully instantiate an empty BinaryTree
def test_create_BT():
    assert Node
    assert BinaryTree
    
# 1a. Passes--Can successfully instantiate an empty BinarySearchTree
def test_create_BST():
    assert Node
    assert BinarySearchTree

# 2. Passes--Can successfully instantiate a BinaryTree with a single root node
def test_one_node_BT():
    actual = str(BinaryTree('a'))
    expected = 'root:a, left:None, right:None'
    assert actual == expected
    
# # 2a. Passes--Can successfully instantiate a BinarySearchTree with a single root node
def test_one_node_BST():
    actual = str(BinarySearchTree(11))
    expected = 'root:11, left:None, right:None'
    assert actual == expected
    
# 3. ***** Both pass when add is in BT class, but not when in  BST class
# and not smooshed together to add two nodes at once ******
# Can successfully add a left child and right child to a single root node

def test_BST_add_left_kid():
    
    actual = str(BinarySearchTree.add('a','left','b'))
    expected = 'root:a, left:b, right:None'
    assert actual == expected


def test_BST_add_right_kid():
    
    actual = str(BinarySearchTree.add('a','right','c'))
    expected = 'root:a, left:None, right:c'
    assert actual == expected
    
# def test_BT_add_both_kids():
#     BT = BinaryTree.add('a', 'left' ,'b')
#     BT.add('a', 'right' ,'c')
    
#     actual = str(BT)
#     expected = 'root:a, left:b, right:c'
#     assert actual == expected
    

# 3a. Can successfully add a left child and right child to a single root node
# def test_BST_add_two_kids():


# 4. Can successfully return a collection from a pre_order traversal
# def test_pre_order(create_tree):
    
#     actual = str(BinaryTree.pre_order(create_tree))
#     expected = [11,10,13]

# 4.a Can successfully return a True Boolean for BST pre_order search of an input

# 4.a.1. Can successfully return a False Boolean for BST pre_order search of an input

# 5. Can successfully return a collection from an inorder traversal

# 5a. Can successfully return a True Boolean for BST in_order search of an input

# 5a.1. Can successfully return a False Boolean for BST in_order search of an input

# 6. Can successfully return a collection from a post_order traversal

# 6a. Can successfully return a True Boolean for BST post_order search of an input

# 6a.1. Can successfully return a False Boolean for BST post_order search of an input



# @pytest.fixture
# def create_tree():
#     """ instantiate and fill a small BT--see visual in images """
#     tree = BinaryTree(Node(11))
#     tree.add = Node(10, left)
#     # tree.root.left.left = Node(9)
#     # tree.root.left.right = Node(12)
#     tree.add = Node(13, right)
#     # tree.root.right.left = Node(7)
#     # tree.root.right.right = Node(15)
#     return tree