# Tree Implementation

## PR for this file: https://github.com/kimmyd70/data-structures-and-algorithms/pull/57

This is code challenge 13 of 401-Python (seattle-py-401n2)

Developers: Kim Damalas

Date: 18 January 2021
____________________
### Challenge 

1. Your function should take a string as its only argument, and should return a boolean representing whether or not the brackets in the string are balanced. There are 3 types of brackets:

Round Brackets : ()

Square Brackets : []

Curly Brackets : {}
__________

## Approach & Efficiency

Approach is using a dictionary, comparison `if` statements and looping as laid out on **Whiteboard** below


Time: O(1) -- traverse the entire string and manipulate a directory

Space: O(1) -- not adding, removing, or changing anything in the input string

_____________
## Required Testing

1. Can successfully validate and return `True` for matched brackets of:
    - Round
    - Square
    - Curly
   
2. Can successfully return `False` for opening bracket without closing bracket

3. Can successfully return `False` for closing bracket without opening bracket

4. Can successfully return `False` for opening bracket and closing brackets of different types
_________________


![Whiteboard](./assets/multi-bracket-validation-whiteboard.png)

