import math

# Roger wanted us to do iteration to see difference
def brute_force(sorted_array, key):
    # for i in range(len(sorted_array)):
    for index, value in enumerate(sorted_array): 
        if value == key:
            return index
            break
        
        

def binary_search(list,key):
    lower = 0
    upper = math.ceil(len(list)/2)
    

