# Quick Sort
Code Challenge 28

 PR located at: https://github.com/kimmyd70/data-structures-and-algorithms/pull/64

 _______________

Given the pseudocode in [algorithm.md](./images/algorithm.md), we'll trace the algorithm 

```
ALGORITHM QuickSort(arr, left, right)
    if left < right
        // Partition the array by setting the position of the pivot value 
        DEFINE position <-- Partition(arr, left, right)
        // Sort the left
        QuickSort(arr, left, position - 1)
        // Sort the right
        QuickSort(arr, position + 1, right)

ALGORITHM Partition(arr, left, right)
    // set a pivot value as a point of reference
    DEFINE pivot <-- arr[right]
    // create a variable to track the largest index of numbers lower than the defined pivot
    DEFINE low <-- left - 1
    for i <- left to right do
        if arr[i] <= pivot
            low++
            Swap(arr, i, low)

     // place the value of the pivot location in the middle.
     // all numbers smaller than the pivot are on the left, larger on the right. 
     Swap(arr, right, low + 1)
    // return the pivot index point
     return low + 1

ALGORITHM Swap(arr, i, low)
    DEFINE temp;
    temp <-- arr[i]
    arr[i] <-- arr[low]
    arr[low] <-- temp

```


using the Sample Array
`[8,4,23,42,16,15]`
___________________

Like merge_sort, this algoritm divides the array into portions and sorts those portions using the `partition` function.  I've chosen to represent the process using the last element as the pivot, but the flexibility built into this method allows any element to be the pivot (vs merge_sort where the sort pivots on the middle point). 

The pivot point is key to the sort in that all smaller elements come before the pivot and larger are placed after the pivot.

You can see the visual here:

![quick sort visual](./quick-sort-visual.png)

Start: 

set pivot point at end of list; set high = n-1 = 5, low = 0
____________

___________________

Step 1: 

The algorithm finds values < pivot and swaps arr[2] (pivot) with arr[n-1]

_______________________

Step 2: 

Recursively sort left of the pivot

____________

___________________

Step 3: 

Recursively sort right of the pivot
____________

______________
### Efficiency
Time: O(nlog2n)--
The algortihm splits the input array recursively, pivots, and sorts. Since the pivot moves the total number of partition operations performed by this function is log2n. Since quick_sort() is called for each portion each time, we get a total runtime of O(n log2n). 

Space: O(1)--
No additional space is being created. This list is being sorted in place…keeping the space at constant O(1).


