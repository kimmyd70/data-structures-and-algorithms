
def merge_sort(arr):
    n = len(arr)
    left = []
    right = []
    if len(arr) == 0:
        return 'cannot sort an empty array'


    elif n > 1:
        mid = n//2
        print(f"{mid} mid")
        # for index in range(0,mid):
        #     left.append(arr[index])
        
        # for index in range(mid,n):
        #     right.append(arr[index])
        
        left = arr[:mid]
        right = arr[mid:]
        print(f"left {left}")
        print(f"right {right}")

            
        #   sort the left side
        merge_sort(left)
        #   sort the right side
        merge_sort(right)
        #   merge the sorted left and right sides together
        merge(left, right, arr)
    

def  merge(left, right, arr):
    i = 0
    j = 0
    k = 0
        

    while i < len(left) and j < len(right):
        print(f"while i,j,k {i,j,k}")
        print(f" left while {left}")
        print(f" right while {right}")
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
            
        k += 1
        print(f"while array {arr}")
        print(f"i,j,k {i,j,k}")

    if i == len(left):
        # set remaining entries in arr to remaining values in right
        for index in range (i,len(right)):
            arr[index-1] = right[index-1]
    else:
        # set remaining entries in arr to remaining values in left
        for index in range (i,len(left)):
            arr[index-1] = left[index-1]

    return arr

if __name__ == "__main__":
    array = [8,4,23,42,16,15]
    merge_sort(array)