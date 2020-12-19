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
    lower = 0
    upper = math.ceil(len(list)/2)
    

