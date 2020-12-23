# Singly Linked List--extended for insertions

## PR for this file: https://github.com/kimmyd70/data-structures-and-algorithms/pull/48
This is code challenge 01 of 401-Python (seattle-py-401n2)

Developers: Kim Damalas with Nick Dorkins  

Date: 19 December 2020
____________________
## Challenge

1. Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.

2. Within your LinkedList class, include a head property. Upon instantiation, an empty Linked List should be created.

3. Define a method called `insert` which takes any value as an argument and adds a new node with that value to the head of the list with an O(1) Time performance.

4. Define a method called includes which takes any value as an argument and returns a boolean result depending on whether that value exists as a Node’s value somewhere within the list.

5. Define a method called toString (or __str__ in Python) which takes in no arguments and returns a string representing all the values in the Linked List, formatted as:
"{ a } -> { b } -> { c } -> NULL"

6. Any exceptions or errors that come from your code should be semantic, capturable errors. For example, rather than a default error thrown by your language, your code should raise/throw a custom, semantic error that describes what went wrong in calling the methods you wrote for this lab.
__________

## Approach & Efficiency

Approach is using classes and their methods to instantiate, traverse, and manipulate our linked list

This function has O(n) time and space efficiency except for adding a node at the head which is O(1)

_____________
## Required Testing

1. Can successfully instantiate an empty linked list

2. Can properly insert into the linked list

3. The head property will properly point to the first node in the linked list

4. Can properly insert multiple nodes into the linked list

5. Will return true when finding a value within the linked list that exists

6. Will return false when searching for a value in the linked list that does not exist

7. Can properly return a collection of all the values that exist in the linked list