# Merge Sort
Code Challenge 27

 PR located at: https://github.com/kimmyd70/data-structures-and-algorithms/pull/63

 _______________

Given the pseudocode in [algorithm.md](./images/algorithm.md), we'll trace the algorithm 

```
ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length
           
    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1
            
        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left
```


using the Sample Array
`[8,4,23,42,16,15]`
___________________

Step 1: Separate original list and start left half sort

First we break the original list into halves: `[8,4,23,42]` and `[42,16,15]`.  We continue to split the left half until it consists of one element on the right and one on the left. These 2x single element halves are fed into merge(), yielding:  `[4,8,...]`. 

NOTE: Mergesort() is a recursive function whose recursive behavior can be seen in the repetitive splitting of the left half (in this case)

![Sorted Left Half of original](./images/start-sort-left.png)

____________

___________________

Step 2: Finish sort of left half of original list

Next we step back once in left sorting algorithm to sort and merge the right 2 elements of the original left half with the newly sorted left 2 elements of the left half.  This gives us the sorted left half of the original list: `[4,8,23,42]`.  The picture above along with the top portion of this picture finishes up the left half of the original list.

![Finished left half of original list](./images/sort-right.png)

_______________________

Step 3: Sort right half of original list

In step 3 we sort the right half of the original list and `[42,16,15]` becomes `[15,16,42]`.  The bottom half of the picture below shows the sorting progression for the right half.

NOTE: As with the left half, mergesort() is a recursive function whose recursive behavior can be seen in the repetitive splitting of the right half (in this case)


![Sorted right half of the original list](./images/sort-right.png)

____________

___________________

Step 4: Merge the sorted left and right halves

Step 4 merges the sorted left half: `[4,8,23]` and the sorted right half: `[15,16,42]` to put the original list back together but now in order: `[4,8,15,16,23,42]`.  The picture below shows each iteration of the merge() function.

![Merge sorted left and right](./images/final-merge.png)
____________

______________
### Efficiency
Time: O(nlog2n)--
The second step splits the input array recursively and calls merge() for each half. Since the array is halved until a single element remains, the total number of halving operations performed by this function is log2n. Since merge() is called for each half, we get a total runtime of O(n log2n). 

Space: O(1)--
No additional space is being created. This list is being sorted in place…keeping the space at constant O(1).


** (analysis taken directly from [realpython.com](https://realpython.com/sorting-algorithms-python/#the-merge-sort-algorithm-in-python))