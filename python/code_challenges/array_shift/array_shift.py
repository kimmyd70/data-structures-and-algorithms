import math

""" A program to insert a number at the middle index of the list"""

def insertShiftArray (list,num):
    new_index = math.ceil(len(list)/2)
    list.insert(new_index, num)
    return list