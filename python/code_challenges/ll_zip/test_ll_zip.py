from ll_zip import LinkedList, Node
zip_lists = LinkedList.zip_lists
import pytest


#passes
def test_import():
    """ proof of life test passes"""
    assert LinkedList
    assert Node
    
#passes
def test_empty():
    """ test 2 empty lists passed in"""
    L1 = []
    L2 = []
    actual = zip_lists(L1,L2)
    expected = 'Cannot zip two empty lists'
    assert actual == expected
    
#
def test_happy(generate_new_list,generate_new_list2):
    """ test 2 lists of equal length """
    actual = zip_lists(generate_new_list,generate_new_list2)
    expected = generate_new_list.head
    assert actual == expected
    
#   
def test_first_empty(generate_new_list2):
    """ test list 1 is empty """
    L1 = []
    actual = zip_lists(L1,generate_new_list2)
    expected = generate_new_list2.head
    assert actual == expected
    
#    
def test_second_empty(generate_new_list):
    """ test list 1 is empty """
    L2 = []
    actual = zip_lists(generate_new_list, L2)
    expected = generate_new_list.head
    assert actual == expected
    

@pytest.fixture
def generate_new_list():
    """ generates new_list of [1,2,3,4] """
    node = Node(0)
    new_list = LinkedList(node)
    list_length = 0
    
    for value in range(1,5):
        new_list.insert(value)
        list_length += 1
    
    return new_list

@pytest.fixture
def generate_new_list2():
    """ generates new_list of [2,3,4,5] """
    node = Node(0)
    new_list = LinkedList(node)
    list_length = 0
    
    for value in range(2,6):
        new_list.insert(value)
        list_length += 1
    
    return new_list
