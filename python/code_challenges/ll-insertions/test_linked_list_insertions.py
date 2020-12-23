from linked_list import LinkedList, Node
import pytest


def test_import():
    """ proof of life test passes"""
    assert LinkedList
    assert Node

# initiate and empty list -- passes
def test_new_empty():
    empty_list = LinkedList()
    actual = empty_list.head
    expected = None
    assert actual == expected

# insert into linked list and 
# head properly points to first node in list -- both pass
def test_insert(generate_new_list):
    generate_new_list.insert(17)
    actual = generate_new_list.head.value
    expected = 17
    assert actual == expected
    
# returns true when value in list is found -- passes
def test_includes(generate_new_list):
    actual = generate_new_list.includes(4)
    expected = True
    assert actual == expected
    
# # returns false when value not in list -- passes
def test_includes_not_found(generate_new_list):
    actual = generate_new_list.includes(7)
    expected = False
    assert actual == expected

# returns collection all values in list -- passes 
# but not entirely sure why it's backwards
def test_insert_many(generate_new_list):
    actual = generate_new_list.insert_many()
    expected = [4,3,2,1]
    assert actual == expected
    
    

@pytest.fixture
def generate_new_list():
    node = Node(0)
    new_list = LinkedList(node)
    list_length = 0
    
    for value in range(1,5):
        new_list.insert(value)
        list_length += 1
    
    return new_list
