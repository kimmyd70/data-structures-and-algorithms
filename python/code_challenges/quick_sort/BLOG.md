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

Step 1: 

____________

___________________

Step 2: 

_______________________

Step 3: 

____________

___________________

Step 4: 
____________

______________
### Efficiency
Time: O(nlog2n)--
The second step splits the input array recursively and calls merge() for each half. Since the array is halved until a single element remains, the total number of halving operations performed by this function is log2n. Since merge() is called for each half, we get a total runtime of O(n log2n). 

Space: O(1)--
No additional space is being created. This list is being sorted in place…keeping the space at constant O(1).


** (analysis taken directly from [realpython.com](https://realpython.com/sorting-algorithms-python/#the-merge-sort-algorithm-in-python))