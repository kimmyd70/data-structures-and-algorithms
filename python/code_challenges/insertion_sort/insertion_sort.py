def insertion_sort(arr):
    if len(arr) == 0:
        return 'cannot sort an empty array'
    
    else:
        for i in range(1,len(arr)):
    
            j = i-1
            temp = arr[i]

            while j >= 0 and temp < arr[j]:
                arr[j + 1] = arr[j]
                j = j - 1
            
            arr[j + 1] = temp
            # print(arr,temp)
        return arr,temp
    
# if __name__ == "__main__":
#     array = [8,4,23,42,16,15]
#     insertion_sort(array)