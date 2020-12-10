# Shift an Array
This is code challenge 01 of 401-Python (seattle-py-401n2)

Developers: Kim Damalas 

Date: 10 December 2020
____________________
## Challenge

Write a function called `insertShiftArray` which takes in an array and the value to be added. Without utilizing any of the built-in methods available to your language, return an array with the new value added at the middle index.
__________

## Approach & Efficiency

We chose to use a function called `insertShiftArray` that determines the length of the array, determines the middle index, and inserts the new value at array(middle+1)

___________

## Solution

First we checked for edge cases of an empty array with `if statements` 

In the case of an array of odd length, we chose the middle as the index closer to the front and added one to insert the new value:

Example: [2,3,4] middle is index = 1 so insertion gives [2,3,new_value,4]

NOTE: this approach works for a single element array. 

Example: [1] becomes [1,new_value]

xxxxxxxxxxxxxx

1. We first looped through the array to count the length

2. Next, we calculated the middle of the array by dividing length by 2, adding +1, and inserting the new value 

- for an odd length, we used length/2 and truncated to the whole integer then +1 for the new value position

- we chose to mutate the original array 

When we finished inserting the new value, we returned the amended array including the new value
_____________
## Testing

We used unit tests as discussed in class to iterate our software build in small steps.  The tests are found in the [Test Code File](./test_array_shift.py)
_______________

Our whiteboarding session:

![Whiteboard Shift-Array](./assets/array-shift-whiteboard.png)

