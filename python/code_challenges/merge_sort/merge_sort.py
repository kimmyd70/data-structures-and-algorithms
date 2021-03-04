

def merge_sort(arr):
    n = len(arr)
    left = []
    right = []

    if n > 1:
        mid = n//2
        
        for index in range(0,mid):
            left.append(arr[index])
        
        for index in range(mid,n-1):
            right.append(arr[index])
            
        #   sort the left side
        merge_sort(left)
        print(left)
        #   sort the right side
        merge_sort(right)
        print(right)
        #   merge the sorted left and right sides together
        merge(left, right, arr)
    

def  merge(left, right, arr):
    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
            
        k += 1

    if i == len(left):
        # set remaining entries in arr to remaining values in right
        for index in range (i,len(right)):
            arr.append(right[index])
    else:
        # set remaining entries in arr to remaining values in left
        for index in range (i,len(left)):
            arr.append(left[index])

    return arr

if __name__ == "__main__":
    array = [8,4,23,42,16,15]
    merge_sort(array)