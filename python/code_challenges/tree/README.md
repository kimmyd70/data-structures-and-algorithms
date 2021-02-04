# Tree Implementation

Developer: Kim Damalas

## PR for this file: https://github.com/kimmyd70/data-structures-and-algorithms/pull/58

This is code challenge 15 of 401-Python (seattle-py-401n2)

Date: 30 January 2021

## PR for this file: https://github.com/kimmyd70/data-structures-and-algorithms/pull/59

Extended with Code Challenge 16 of 401-Python
(seattle-py-401n2)

Update: 4 February 2021
____________________
### Challenge 

1. Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.

2. Create a BinaryTree class

    - Define a method for each of the depth first traversals called `preOrder`, `inOrder`, and `postOrder` which returns an array of the values, ordered appropriately.

3. Create a BinarySearchTree class

    - Define a method named `add` that accepts a value, and adds a new node with that value in the correct location in the binary search tree.

    - Define a method named `contains` that accepts a value, and returns a boolean indicating whether or not the value is in the tree at least once.

4. Any exceptions or errors that come from your code should be semantic, capturable errors. For example, rather than a default error thrown by your language, your code should raise/throw a custom, semantic error that describes what went wrong in calling the methods you wrote for this lab.

____________

5. UPDATE: Write an instance method called `find-maximum-value`. Without utilizing any of the built-in methods available to your language, return the maximum value stored in the tree. You can assume that the values stored in the Binary Tree will be numeric.
__________

## Approach & Efficiency

Approach is using Nodes, Classes, and Class methods as described above


Time:   O(n) -- traverse the entire tree or inserting a node
        O(log n)-- if binary tree perfectly balanced

Space:  O(width) -- max width
        2^((log n)-1) -- perfectly balanced tree
        O(1) -- for binary search

`find-maximum-value`
Time: O(n) -- may need to traverse entire tree
Space: O(1) -- storing one variable and replacing

_____________
## Required Testing

1. Can successfully instantiate an empty tree
2. Can successfully instantiate a tree with a single root node
3. Can successfully add a left child and right child to a single root node
4. Can successfully return a collection from a preorder traversal
5. Can successfully return a collection from an inorder traversal
6. Can successfully return a collection from a postorder traversal

-----------
No tests required from CC#16 assignment, but write unit test to capture:
1. happy path
2. known failure
3. edge cases (empty tree, one node tree, 3 node tree all same value, negative numbers present; float values will behave the same as int because of python operator defaults)
_________________

## Whiteboard

CC#16
![Find Max Value Whiteboard](./images/find-max-value-whiteboard.png)

