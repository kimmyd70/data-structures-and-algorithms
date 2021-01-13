# Stack and Queue Implementation

## PR for this file: https://github.com/kimmyd70/data-structures-and-algorithms/pull/54

This is code challenge 10 of 401-Python (seattle-py-401n2)

Developers: Kim Damalas

Date: 13 January 2021
____________________
### Challenge -- Stacks

1. Create a `Node` class that has properties for the value stored in the Node, and a pointer to the next node.

2. Create a `Stack` class that has a top property. It creates an empty Stack when instantiated.

    - This object should be aware of a default empty value assigned to top when the stack is created.

    - Define a method called `push` which takes any value as an argument and adds a new node with that value to the top of the stack with an O(1) Time performance.

    - Define a method called `pop` that does not take any argument, removes the node from the top of the stack, and returns the node’s value.

        - Should raise exception when called on empty stack

    - Define a method called `peek` that does not take an argument and returns the value of the node located on top of the stack, without removing it from the stack.

        - Should raise exception when called on empty stack

    - Define a method called `is_empty` that takes no argument, and returns a boolean indicating whether or not the stack is empty.

### Challenge -- Queues

3. Create a `Queue` class that has a front property. It creates an empty Queue when instantiated.

    - This object should be aware of a default empty value assigned to front when the queue is created.

    - Define a method called `enqueue` which takes any value as an argument and adds a new node with that value to the back of the queue with an O(1) Time performance.

    - Define a method called `dequeue` that does not take any argument, removes the node from the front of the queue, and returns the node’s value.

        - Should raise exception when called on empty queue

    - Define a method called `peek` that does not take an argument and returns the value of the node located in the front of the queue, without removing it from the queue.

        - Should raise exception when called on empty queue

    - Define a method called `is_empty` that takes no argument, and returns a boolean indicating whether or not the queue is empty.

Be sure to follow your languages best practices for naming conventions.

__________

## Approach & Efficiency

Approach is using classes and their methods to instantiate and manipulate our stacks and queues.  

Time: O(n) -- worst case assumes  we must traverse the entire list

Space: O(1) -- adding or removing from stack or queue, peek, and is_empty method.

_____________
## Required Testing

1. Can successfully push onto a stack
2. Can successfully push multiple values onto a stack
3. Can successfully pop off the stack
4. Can successfully empty a stack after multiple pops
5. Can successfully peek the next item on the stack
6. Can successfully instantiate an empty stack
7. Calling pop or peek on empty stack raises exception
8. Can successfully enqueue into a queue
9. Can successfully enqueue multiple values into a queue
10. Can successfully dequeue out of a queue the expected value
11. Can successfully peek into a queue, seeing the expected value
12. Can successfully empty a queue after multiple dequeues
13. Can successfully instantiate an empty queue
14. Calling dequeue or peek on empty queue raises exception


_________________


