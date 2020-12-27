
from array_binary_search import brute_force,binary_search


# Roger wanted us to do iteration to see difference
# This test passes
def test_brute_force():
    actual = brute_force([1,2,6,7,8,9,10],2)
    expected = 1
    assert actual == expected
    

    
# # key not in empty array -- passes
def test_empty():
    actual = binary_search([], 2)
    expected = -1
    assert actual == expected
    
#  key not in the array (w/values) --passes
def test_no_match():
    actual = binary_search([1,3,6,7,8,9,10], 2)
    expected = -1
    assert actual == expected
      
# # key in the array w/large array (odd num elements)--passes
def test_lg():
    actual = binary_search([6,7,8,9,10,12,16,19,20], 12)
    expected = 5
    assert actual == expected
    
# # key in the array w/large array (even num elements)--passes
def test_even():
    actual = binary_search([7,8,9,10,12,16,19,20], 12)
    expected = 4
    assert actual == expected
