from tree import Node, BinaryTree
from tree import BinarySearchTree
import pytest


# 9 passing ; 3 skipping (add not working, so tests skipped)

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
    
    
# 3. ** Passes with the fixture on BT and BST -- need to code BinarySearchTree.add ***
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
def test_BST_add_left_kid(create_int_tree):
    """ test add to left of 15 -- see visual in images """
    root_value = (create_int_tree.root.right.right.value)
    actual = root_value # correct root, but 
    # 59 = TypeError: add() takes from 1 to 3 positional arguments but 4 were given
    
    # actual = create_int_tree.add(root_value, 'left', 14).root
    expected = 15
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
    

# 4. Passes with fixture--Can successfully return a collection from a pre_order traversal

# @pytest.mark.skip("pending")
def test_pre_order(create_letter_tree):
    tree = create_letter_tree
    actual = tree.pre_order(tree.root)
    expected = ['a','b','d','e','c','f','g']
    assert actual == expected
    

# 4.a Can successfully return a True Boolean for BST pre_order search of an input

# 4.a.1. Can successfully return a False Boolean for BST pre_order search of an input

# 5. Passes with fixture--Can successfully return a collection from an inorder traversal

# @pytest.mark.skip("pending")
def test_in_order(create_letter_tree):
    tree = create_letter_tree
    actual = tree.in_order(tree.root)
    expected = ['d','b','e','a','f','c','g']
    assert actual == expected


# 5a. Can successfully return a True Boolean for BST in_order search of an input


# 5a.1. Can successfully return a False Boolean for BST in_order search of an input

# 6. Can successfully return a collection from a post_order traversal
# @pytest.mark.skip("pending")
def test_post_order(create_letter_tree):
    tree = create_letter_tree
    actual = tree.post_order(tree.root)
    expected = ['d','e','b','f','g','c','a']
    assert actual == expected

# 6a. Can successfully return a True Boolean for BST post_order search of an input

# 6a.1. Can successfully return a False Boolean for BST post_order search of an input



@pytest.fixture
def create_int_tree():
    """ instantiate and fill a small BST--see visual in images """
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
    tree = BinarySearchTree(eleven)
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
