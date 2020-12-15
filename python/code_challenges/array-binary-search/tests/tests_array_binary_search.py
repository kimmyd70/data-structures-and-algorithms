from array_binary_search import __version__
from array_binary_search import *


def test_version():
    assert __version__ == '0.1.0'
    
# key not in empty array
def test_empty():
    actual = binary_search([], 2)
    expected = -1
    assert actual == expected
    
#  key not in the array (w/values)
def test_no_match():
    actual = binary_search([1,3,6.7.8.9,10], 2)
    expected = -1
    assert actual == expected
    
# key in the array w/small array (odd num elements)
def test_small():
    actual = binary_search([1,2,6.7.8.9,10], 2)
    expected = 1
    assert actual == expected
    
# key in the array w/large array (odd num elements)
def test_lg():
    actual = binary_search([6,7,8,9,10,12,16,19,20], 12)
    expected = 5
    assert actual == expected
    
# key in the array w/large array (even num elements)
def test_even():
    actual = binary_search([7,8,9,10,12,16,19,20], 12)
    expected = 4
    assert actual == expected
