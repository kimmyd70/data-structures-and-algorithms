from tree import Node, BinaryTree, BinarySearchTree


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
    expected = f'BT left: {{ 7 }} ->  and right: {{ 7 }} -> '
    assert actual == expected
    
# 2a. Can successfully instantiate a BinaryTree with a single root node
def test_one_node_BST():
    node = Node(9)
    actual = str(BinarySearchTree(node))
    expected = f'{{ 9 }} ->'

# 3. Can successfully add a left child and right child to a single root node
# 4. Can successfully return a collection from a preorder traversal
# 5. Can successfully return a collection from an inorder traversal
# 6. Can successfully return a collection from a postorder traversal

