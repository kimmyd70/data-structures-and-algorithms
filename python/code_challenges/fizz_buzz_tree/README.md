# Fizz Buzz Tree Implementation

Developer: Kim Damalas

## PR for this file: https://github.com/kimmyd70/data-structures-and-algorithms/pull/61

This is code challenge 18 of 401-Python (seattle-py-401n2)

Date: 8 Feb 2021

____________________
### Challenge 

1. Write a function called `FizzBuzzTree` which takes a k-ary tree as an argument.

2. Without utilizing any of the built-in methods available to your language, determine whether or not the value of each node is divisible by 3, 5 or both. Create a new tree with the same structure as the original, but the values modified as follows:

    - If the value is divisible by 3, replace the value with “Fizz”

    - If the value is divisible by 5, replace the value with “Buzz”

    - If the value is divisible by 3 and 5, replace the value with “FizzBuzz”

    - If the value is not divisible by 3 or 5, simply turn the number into a String (my choice: "Neither").

3. Return a new tree.
____________

## Approach & Efficiency

Approach is using Nodes, A Tree Class, and Class methods to create a new tree with different node values as stated in 3)


Time:   O(n) -- traverse the entire tree 
        

Space:  O(n) -- create a new tree
        O(1) -- if instructions didn't require a new tree, I'd replace values and not create new storage structure

_____________
## Required Testing

No tests required from CC#18 assignment, but write unit test to capture:
1. happy path
2. known failure
3. edge cases 
_________________

## Whiteboard

CC#18
![Fizz-Buzz-Tree-Whiteboard](./assets/fizz-buzz-tree-whiteboard.png)
