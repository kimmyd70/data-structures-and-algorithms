# from array_shift import __version__
from array_shift import *

#proof of life
# def test_version():
#     assert __version__ == '0.1.0'


# base case with empty array
def test_base():
    actual = insertShiftArray([], 2)
    expected = [2]
    assert actual == expected

# base case with one element array
def test_one_element():
    actual = insertShiftArray([1], 2)
    expected = [1,2]
    assert actual == expected

# test case with odd number of array elements
def test_odd():
    actual = insertShiftArray([1,3,5,7,9], 2)
    expected = [1,3,5,2,7,9]
    assert actual == expected

# test case with even number of array elements
def test_even():
    actual = insertShiftArray([1,3,5,7], 2)
    expected = [1,3,2,5,7]
    assert actual == expected


