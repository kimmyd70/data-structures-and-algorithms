# Queues With Stacks

## PR for this file: https://github.com/kimmyd70/data-structures-and-algorithms/pull/55

This is code challenge 11 of 401-Python (seattle-py-401n2)

Developers: Kim Damalas

Date: 13 January 2021
____________________
### Challenge 

1. Create a brand new `PseudoQueue` class. Do not use an existing Queue. Instead, this PseudoQueue class will implement our standard queue interface (the two methods listed below), but will internally only utilize 2 Stack objects. Ensure that you create your class with the following methods:

- enqueue(value) which inserts value into the PseudoQueue, using a first-in, first-out approach

- dequeue() which extracts a value from the PseudoQueue, using a first-in, first-out approach

- The Stack instances have only push, pop, and peek methods. You should use your own Stack implementation

- Instantiate these Stack objects in your PseudoQueue constructor
__________

## Approach & Efficiency

Approach is using classes and their methods to instantiate and manipulate our stacks and queues.  

Time: O(n) -- worst case assumes  we must traverse the entire list

Space: O(1) -- adding or removing from stack or queue, peek, and is_empty method.

_____________
## Required Testing

1. Can successfully enqueue into an empty PseudoQueue

2. Can successfully dequeue out of a queue the expected value

3. Can successfully instantiate an empty PseudoQueue

4. Calling dequeue on empty queue raises exception


_________________

![Whiteboard](./assets/queues-with-stacks-whiteboard.png)