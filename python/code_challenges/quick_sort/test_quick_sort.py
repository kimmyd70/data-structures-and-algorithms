import pytest
from quick_sort import *

# all tests pass
# @pytest.mark.skip("pending")  
def test_quick_sort_empty():
    array = []
    actual = quick_sort(array,0,len(array)-1)
    expected = 'cannot sort an empty array'
    assert actual == expected


# @pytest.mark.skip("pending")
def test_quick_sort_happy():
    array = [8,4,23,42,16,15]
    actual = quick_sort(array,0,len(array)-1)
    expected = [4,8,15,16,23,42]
    assert actual == expected
    
# @pytest.mark.skip("pending")
def test_quick_sort_dupes():
    array = [8,4,4,4,16,5]
    actual = quick_sort(array,0,len(array)-1)
    expected = [4,4,4,5,8,16]
    assert actual == expected
    
    
# @pytest.mark.skip("pending")  
def test_quick_sort_long():
    array = [4,6,2,4,8,7,1,12,3]
    actual = quick_sort(array,0,len(array)-1)
    expected = [1,2,3,4,4,6,7,8,12]
    assert actual == expected
    
# @pytest.mark.skip("pending")  
def test_quick_sort_short():
    array = [4,6,2]
    actual = quick_sort(array,0,len(array)-1)
    expected = [2,4,6]
    assert actual == expected