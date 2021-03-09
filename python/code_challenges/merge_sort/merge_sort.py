
def merge_sort(arr):
    n = len(arr)
    if len(arr) == 0:
        return 'cannot sort an empty array'
    
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
            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1
        else:
            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1

        return arr
        
    if n > 1:
        mid = n//2
        # for index in range(0,mid):
        #     left.append(arr[index])
        
        # for index in range(mid,n):
        #     right.append(arr[index])
        
        left = arr[:mid]
        right = arr[mid:]

            
        #   sort the left side
        merge_sort(left)
        #   sort the right side
        merge_sort(right)
        #   merge the sorted left and right sides together
        return merge(left, right, arr)
    else:
        return arr

#  Code block order changed with help from Ashley Casimir


if __name__ == "__main__":
    array = [8,4,23,42,16,15]
    merge_sort(array)
    print(array)