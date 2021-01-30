from tree import Node, BinaryTree, BinarySearchTree


# 1. Passes--Can successfully instantiate an empty tree
def test_import():
    assert Node
    assert BinaryTree
    
# 2. Passes--Can successfully instantiate a tree with a single root node
def test_one_node_tree():
    node = Node(7)
    actual = str(BinaryTree(node))
    expected = f'{{ 7 }} ->'
    
    
# 3. Can successfully add a left child and right child to a single root node
# 4. Can successfully return a collection from a preorder traversal
# 5. Can successfully return a collection from an inorder traversal
# 6. Can successfully return a collection from a postorder traversal

