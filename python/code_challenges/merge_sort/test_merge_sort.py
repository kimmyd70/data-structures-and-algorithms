import pytest
from merge_sort import *

# passes
# @pytest.mark.skip("pending")  
def test_merge_sort_empty():
    array = []
    actual = merge_sort(array)
    expected = 'cannot sort an empty array'
    assert actual == expected


# @pytest.mark.skip("pending")
def test_merge_sort_happy():
    array = [8,4,23,42,16,15]
    actual = merge_sort(array)
    expected = [4,8,15,16,23,42]
    assert actual == expected
    
# @pytest.mark.skip("pending")
def test_merge_sort_dupes():
    array = [8,4,4,4,16,5]
    actual = merge_sort(array)
    expected = [4,4,4,5,8,16]
    assert actual == expected
    
    
# @pytest.mark.skip("pending")  
def test_merge_sort_long():
    array = [4,6,2,4,8,7,1,12,3]
    actual = merge_sort(array)
    expected = [1,2,3,4,4,6,7,8,12]
    assert actual == expected
    
# @pytest.mark.skip("pending")  
def test_merge_sort_short():
    array = [4,6,2]
    actual = merge_sort(array)
    expected = [2,4,6]
    assert actual == expected