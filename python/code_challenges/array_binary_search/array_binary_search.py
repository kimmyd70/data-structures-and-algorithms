import math

# Roger wanted us to do iteration to see difference
def brute_force(sorted_array, key):
    # for i in range(len(sorted_array)):
    for index, value in enumerate(sorted_array): 
        if value == key:
            return index
            break
        
        

def binary_search(list,key):
	# Find the length of the array and divide by 2 to get middle index 
    # (Math.ceil to get index to the right of the middle for odd number of elements)
    middle = math.ceil(len(list)/2)
	# set upper bound to len(list) and lower bound to 0
    lower = 0
    upper = len(list)
    
	# check bounds and middle == key
	# - if  value = key; stop search and return index
    
	# Repeat as many times as needed until upper and lower bound indices have a single value between them
    while upper - lower > 1:
        if list.upper.value == key:
            return list.upper.value
        if list.lower.value == key:
            return list.lower.value
        if list.middle.value == key:
            return list.middle.value

        # - if key is higher, set middle index as lower bound and last index as upper bound
        # - if key is lower, set middle index as upper bound and index 0 as lower bound
        
        if middle > key:
            lower = middle
        if middle < key:
            upper = middle
	
	# if value at index between upper and lower bounds == key, stop search and return index
    # captured in while on last loop
	
    # if value at index between upper and lower bounds != key, stop search and return -1
    return -1
