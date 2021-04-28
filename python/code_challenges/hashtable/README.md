# Hashtable Implementation

Developer: Kim Damalas

## PR for this file: https://github.com/kimmyd70/data-structures-and-algorithms/pull/74

This is code challenge 30 of 401-Python (seattle-py-401n2)

Date: 28 April 2021
____________________
### Challenge 

Implement a Hashtable with the following methods:

1. `add`: takes in both the key and value. 
    - This method should hash the key, and add the key and value pair to the table, handling collisions as needed.

2. `get`: takes in the key and returns the value from the table.

3. `contains`: takes in the key and returns a boolean, indicating if the key exists in the table already.

4. `hash`: takes in an arbitrary key and returns an index in the collection.
____________

## Approach & Efficiency

Single-responsibility principle: any methods you write should be clean, reusable, abstract component parts to the whole challenge. 
_____________
## Required Testing

Write unit test to capture:
1. Adding a key/value to your hashtable results in the value being in the data structure

2. Retrieving based on a key returns the value stored

3. Successfully returns null for a key that does not exist in the hashtable

4. Successfully handle a collision within the hashtable

5. Successfully retrieve a value from a bucket within the hashtable that has a collision

6. Successfully hash a key to an in-range value

_________________

## Whiteboard

CC#35 -- no whiteboard for implementation

