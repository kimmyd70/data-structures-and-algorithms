from ll_zip import LinkedList, Node
zip_lists = LinkedList.zip_lists
import pytest


# passes
def test_import():
    """ proof of life test passes"""
    assert LinkedList
    assert Node
    
# passes
def test_empty():
    """ test 2 empty lists passed in"""
    L1 = LinkedList()
    L2 = LinkedList()
    actual = zip_lists(L1,L2)
    expected = 'cannot zip two empty lists'
    assert actual == expected
    
# passes   
# @pytest.mark.skip("pending")
def test_happy():
    """ test 2 lists of equal length """
    L1 = LinkedList()
    L2 = LinkedList()
    L1.insert(1)
    L2.insert(1)
    L1.insert(2)
    L2.insert(2)
    L1.insert(3)
    L2.insert(3)

    actual =  str(zip_lists(L1,L2))
    expected = '{ 3 } -> { 3 } -> { 2 } -> { 2 } -> { 1 } -> { 1 } -> NULL'
    assert actual == expected

# passes    
# @pytest.mark.skip("pending")
def test_second_empty():
    """ test list 2 is empty """
    L1 = LinkedList()
    L2 = LinkedList()
    L1.insert(1)
    L1.insert(2)
    L1.insert(3)

    actual = str(zip_lists(L1,L2))
    expected = 'list 2 empty; list 1 unchanged'
    assert actual == expected
    
# @pytest.mark.skip("pending")
def test_first_empty():
    """ test list 1 is empty """
    L1 = LinkedList()
    L2 = LinkedList()
    L2.insert(4)
    L2.insert(5)
    L2.insert(6)
    
    actual = str(zip_lists(L1,L2))
    expected = 'cannot zip into empty list'
    assert actual == expected
    

# @pytest.fixture
# def generate_new_list():
#     """ generates new_list of [1,2,3,4] """
#     node = Node(0)
#     new_list = LinkedList(node)
#     list_length = 0
    
#     for value in range(1,5):
#         new_list.insert(value)
#         list_length += 1
    
#     return new_list

# @pytest.fixture
# def generate_new_list2():
#     """ generates new_list of [2,3,4,5] """
#     node = Node(0)
#     new_list = LinkedList(node)
#     list_length = 0
    
#     for value in range(2,6):
#         new_list.insert(value)
#         list_length += 1
    
#     return new_list
