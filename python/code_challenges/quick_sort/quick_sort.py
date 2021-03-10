
def quick_sort(arr, low, high):
    if len(arr) == 0:
        return 'cannot sort an empty array'
    
    if len(arr) == 1:
        return arr

    if low < high:
        p = partition(arr, low, high)

        quick_sort(arr, low, p - 1)

        quick_sort(arr, p + 1, high)

    return arr

def partition(arr, low, high):
    pivot = arr[high]
    i = (low -1)

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    print(array)
    return (i + 1)

    
if __name__ == "__main__":
    array = [8,4,23,42,16,15]
    n = len(array)
    quick_sort(array, 0, n-1)
    print (f'sorted: {array}')