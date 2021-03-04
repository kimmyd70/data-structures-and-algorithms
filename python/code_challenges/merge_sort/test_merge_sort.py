import pytest
from merge_sort import *

#### all tests pass ###

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
def test_merge_sort_empty():
    array = []
    actual = merge_sort(array)
    expected = 'cannot sort an empty array'
    assert actual == expected