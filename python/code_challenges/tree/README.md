# Tree Implementation

Developers: Kim Damalas

## PR for this file: https://github.com/kimmyd70/data-structures-and-algorithms/pull/58

This is code challenge 15 of 401-Python (seattle-py-401n2)

Date: 30 January 2021

## PR for this file: https://github.com/kimmyd70/data-structures-and-algorithms/pull/60

This is code challenge 17 of 401-Python (seattle-py-401n2)

Date: 4 Feb 2021
____________________
### Challenge 

1. Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.

2. Create a BinaryTree class

    - Define a method for each of the depth first traversals called `preOrder`, `inOrder`, and `postOrder` which returns an array of the values, ordered appropriately.

3. Create a BinarySearchTree class

    - Define a method named `add` that accepts a value, and adds a new node with that value in the correct location in the binary search tree.

    - Define a method named `contains` that accepts a value, and returns a boolean indicating whether or not the value is in the tree at least once.

4. Any exceptions or errors that come from your code should be semantic, capturable errors. For example, rather than a default error thrown by your language, your code should raise/throw a custom, semantic error that describes what went wrong in calling the methods you wrote for this lab.

----
6. UPDATE: CC#17: Write a `breadth first` traversal method which takes a Binary Tree as its unique input. Without utilizing any of the built-in methods available to your language, traverse the input tree using a Breadth-first approach, and return a list of the values in the tree in the order they were encountered.

__________

## Approach & Efficiency

Approach is using Nodes, Classes, and Class methods as described above


Time:   O(n) -- traverse the entire tree or inserting a node
        O(log n)-- if binary tree perfectly balanced

Space:  O(width) -- max width
        2^((log n)-1) -- perfectly balanced tree
        O(1) -- for binary search

Breadth first should be same Time/Space above
_____________
## Required Testing

1. Can successfully instantiate an empty tree
2. Can successfully instantiate a tree with a single root node
3. Can successfully add a left child and right child to a single root node
4. Can successfully return a collection from a preorder traversal
5. Can successfully return a collection from an inorder traversal
6. Can successfully return a collection from a postorder traversal

_________________

No required testing from CC#17 assignment, but test happy path, known failure, and edge cases.

_________________

## Whiteboard

CC#17
![Whiteboard for Breadth First](./images/breadth-first-whiteboard.png)
