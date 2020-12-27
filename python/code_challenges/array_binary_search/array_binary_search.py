import math

# Roger wanted us to do iteration to see difference
def brute_force(sorted_array, key):
    for index, value in enumerate(sorted_array): 
        if value == key:
            break
        else:
            return -1
        
    return index

def binary_search(list,key):
	# Find the length of the array and divide by 2 to get middle index 
    # (Math.ceil to get index to the right of the middle for odd number of elements)
	# set upper bound to len(list)-1 to get last index and lower bound to 0
    lower = 0
    upper = len(list)-1
    middle = math.ceil(len(list)/2)
    result = -1
    
    # check for empty list
    if not len(list):
        return result
    
    
	# Repeat as many times as needed until upper and lower bound indices have a single value between them
    
    for item in range(lower, len(list) + 1):
	# check bounds and middle == key
	# - if  value = key; stop search and return index
        if list[upper] == key:
            result = upper
        if list[lower] == key:
            result = lower
        if list[middle]== key:
            result = middle
        

        # - if key is higher, set middle index as lower bound and last index as upper bound
        # - if key is lower, set middle index as upper bound and index 0 as lower bound
        if list[middle] > key:
            lower = middle
        if list[middle] < key:
            upper = middle
        
	
    # if value at index between upper and lower bounds != key, stop search and return -1
        if upper == lower:
            result = -1
    # captured if for loop ends without returning anything
        return result
	
        
