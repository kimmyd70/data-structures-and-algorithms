from tree import Node, BinaryTree 
from tree import BinarySearchTree

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
    node = Node(7)
    actual = str(BinaryTree(node))
    expected = 'BT left: [7] and right: [7]'
    assert actual == expected
    
# 2a. Passes--Can successfully instantiate a BinarySearchTree with a single root node
def test_one_node_BST():
    node = Node(9)
    actual = str(BinarySearchTree(node))
    expected = 'BST left: [9] and right: [9]'
    assert actual == expected

# 3. Can successfully add a left child and right child to a single root node
# def test_BT_add_two_kids():

# 3a. Can successfully add a left child and right child to a single root node
# def test_BST_add_two_kids():


# 4. Can successfully return a collection from a pre_order traversal

# 4.a Can successfully return a True Boolean for BST pre_order search of an input

# 4.a.1. Can successfully return a False Boolean for BST pre_order search of an input

# 5. Can successfully return a collection from an inorder traversal

# 5a. Can successfully return a True Boolean for BST in_order search of an input

# 5a.1. Can successfully return a False Boolean for BST in_order search of an input

# 6. Can successfully return a collection from a post_order traversal

# 6a. Can successfully return a True Boolean for BST post_order search of an input

# 6a.1. Can successfully return a False Boolean for BST post_order search of an input



