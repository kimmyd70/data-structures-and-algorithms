from tree import Node, BinaryTree
from tree import BinarySearchTree
import pytest


# 15 tests total

# 1. Passes--Can successfully instantiate an empty BinaryTree
def test_create_empty_BT():
    actual = BinaryTree().root
    expected = None
    assert actual == expected
    
# 1a. Passes--Can successfully instantiate an empty BinarySearchTree
def test_create_empty_BST():
    actual = BinarySearchTree().root
    expected = None
    assert actual == expected
    

# 2. Passes--Can successfully instantiate a BinaryTree with a single root node
def test_one_node_BT():
    actual = BinaryTree(75).root
    expected = 75
    assert actual == expected
    
    
# # 2a. Passes--Can successfully instantiate a BinarySearchTree with a single root node
#@pytest.mark.skip("pending")
def test_one_node_BST():
    actual = BinarySearchTree('a').root
    expected = 'a'
    assert actual == expected
    
    
# 3. ***** Passes with the fixture -- need to code BinarySearchTree.add ******
# Can successfully add a left child and right child to a single root node

# @pytest.mark.skip("pending")
def test_int_fixture(create_int_tree):

    actual = create_int_tree.root.left.value
    expected = 10
    assert actual == expected

# @pytest.mark.skip("pending")
def test_letter_fixture(create_letter_tree):
    actual = create_letter_tree.root.right.value
    expected = 'c'
    assert actual == expected
    
@pytest.mark.skip("pending")
def test_BT_add_left_kid():
    
    actual = BinaryTree.add('a','left','b')
    expected = 
    assert actual == expected



@pytest.mark.skip("pending")
def test_BST_add_right_kid():
    
    actual = str(BinaryTree.add('a','right','c'))
    expected = 'root:a, left:None, right:c'
    assert actual == expected
    
@pytest.mark.skip("pending")
def test_BT_add_both_kids():
    BT = BinaryTree.add('a', 'left' ,'b')
    BT.add('a', 'right' ,'c')
    
    actual = str(BT)
    expected = 'root:a, left:b, right:c'
    assert actual == expected
    

# 3a. Can successfully add a left child and right child to a single root node
# ***** Both pass when add is in BT class, but not when add is in  BST class
# and not smooshed together to add two nodes at once ******
@pytest.mark.skip("pending")
def test_BST_add_two_kids():
    pass


# 4. Can successfully return a collection from a pre_order traversal

@pytest.mark.skip("pending")
def test_pre_order():
    # pre_tree = BinaryTree.add('a','left','b')
    # pre_tree = BinaryTree.add('b','left','c')
    # pre_tree = BinaryTree.add('b','right','d')
    # actual = str(pre_tree.root.left)
    # expected = 'root:a, left:b, right:None'
    pass

# 4.a Can successfully return a True Boolean for BST pre_order search of an input

# 4.a.1. Can successfully return a False Boolean for BST pre_order search of an input

# 5. Can successfully return a collection from an inorder traversal

# 5a. Can successfully return a True Boolean for BST in_order search of an input

# 5a.1. Can successfully return a False Boolean for BST in_order search of an input

# 6. Can successfully return a collection from a post_order traversal

# 6a. Can successfully return a True Boolean for BST post_order search of an input

# 6a.1. Can successfully return a False Boolean for BST post_order search of an input



@pytest.fixture
def create_int_tree():
    """ instantiate and fill a small BT--see visual in images """
    eleven = Node(11)
    ten = Node(10)
    nine = Node(9)
    twelve = Node(12)
    thirteen = Node(13)
    seven = Node(7)
    fifteen = Node(15)
    
    #sub-trees
    ten.left = nine
    ten.right = twelve
    thirteen.left = 7
    thirteen.right = fifteen
    
    #first sub-tree
    tree = BinaryTree(eleven)
    tree.root.left = ten
    tree.root.right = thirteen
  
    return tree

@pytest.fixture
def create_letter_tree():
    """ instantiate and fill a small BT--see visual in images """
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')
    g = Node('g')

    #sub-trees
    b.left = d
    b.right = e
    c.left = f
    c.right = g

    #first sub-tree
    tree = BinaryTree(a)
    tree.root.left = b
    tree.root.right = c
    
    return tree
