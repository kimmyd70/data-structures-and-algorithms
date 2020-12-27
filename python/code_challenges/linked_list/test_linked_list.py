from linked_list import LinkedList, Node, kth_from_end
import pytest

#passes
def test_import():
    """ proof of life test passes"""
    assert LinkedList
    assert Node
    
    
# 1. Where k is greater than the length of the linked list (raise error)
# passes
def test_k_greater():
    node = Node(0)
    link = LinkedList(node)
    link.insert(1)
    link.insert(2)
    link.insert(3)
    link.insert(4)
    link.insert(5)
    
    actual = kth_from_end(link,7)
    expected = 'IndexError: k is too big for your list'
    assert actual == expected

# 2. Where k and the length of the list are the same (return value of head)
# passes
def test_k_equal():
    node = Node(0)
    link = LinkedList(node)
    link.append(1)
    link.append(2)
    link.append(3)
    link.append(4)
    link.append(5)
    
    actual =  kth_from_end(link,6)
    expected = 0
    assert actual == expected


# 3. Where k is not a positive integer (raise error or use absolute value of k ??)
# passes
def test_k_not_positive():
    node = Node(0)
    link = LinkedList(node)
    link.append(1)
    link.append(2)
    link.append(3)
    link.append(4)
    link.append(5)
    
    actual =  kth_from_end(link,-6)
    expected = 'error: k is not positive integer'
    assert actual == expected


# 4. Where the linked list is of a size 1 (k can only be 1 or raise error)
# passes
def test_list_size_one():
    node = Node(0)
    link = LinkedList(node)
    
    actual =  kth_from_end(link,1)
    expected = 0
    assert actual == expected

# passes
def test_list_size_one_k_error():
    node = Node(0)
    link = LinkedList(node)
    
    actual =  kth_from_end(link,3)
    expected = 'IndexError: k is too big for your list'
    assert actual == expected


# 5. “Happy Path” where k is not at the end, but somewhere in the middle 
# of the linked list (any k < list length)
# passes
def test_any_k():
    node = Node(0)
    link = LinkedList(node)
    link.append(7)
    link.append(2)
    link.append(9)
    link.append(4)
    link.append(0)
    
    actual = kth_from_end(link,3)
    
    expected = 9
    assert actual == expected




#########################
## These tests developed for Code Challenge 06 before
## extending LinkedList with the kth value method##
########################


# # add a node to the end of the linked list -- passes
# def test_append ():
#     node = Node(0)
#     link = LinkedList(node)
#     link.insert(4)
#     link.append(10)
#     actual = str(link)
#     expected = f'{{ 4 }} -> {{ 0 }} -> {{ 10 }} -> NULL'
#     assert actual == expected
    
# # insert a node before a node located in the middle of a linked list -- passed
# def test_before ():
#     node = Node(0)
#     link = LinkedList(node)
#     link.insert(4)
#     link.append(10)
#     link.insert_before(0,5)
#     actual = str(link)
#     expected = f'{{ 4 }} -> {{ 5 }} -> {{ 0 }} -> {{ 10 }} -> NULL'
#     assert actual == expected
    
# # insert a node before the first node of a linked list -- passes
#     def test_before_first ():
#         node = Node(0)
#         link = LinkedList(node)
#         link.insert(4)
#         link.append(10)
#         link.insert_before(4,5)
#         actual = str(link)
#         expected = f'{{ 5 }} -> {{ 4 }} ->  {{ 0 }} -> {{ 10 }} -> NULL'
#         assert actual == expected

    
# # insert a node after a node located in the middle of a linked list -- passes
# def test_after ():
#     node = Node(0)
#     link = LinkedList(node)
#     link.append(3)
#     link.append(10)
    
#     link.insert_after(3,5)
#     actual = str(link)
#     expected = f'{{ 0 }} -> {{ 3 }} -> {{ 5 }} -> {{ 10 }} -> NULL'
#     assert actual == expected
    
# # insert a node after the last node of the linked list -- passes
# ###### how is this not the same as testing the .append function? ######
# def test_after_last ():
#     node = Node(0)
#     link = LinkedList(node)
#     link.append(3)
#     link.append(10)
    
#     link.append(5)
#     actual = str(link)
#     expected = f'{{ 0 }} -> {{ 3 }} -> {{ 10 }} -> {{ 5 }} -> NULL'
#     assert actual == expected

    
# # add multiple nodes to the end of a linked list -- passes
# # method returns tuple with 2 elements: the list dunder string, list_length
# def test_insert_many():
#     node = Node(0)
#     link = LinkedList(node)

#     actual = link.insert_many()
#     expected =  ('{ 4 } -> { 3 } -> { 2 } -> { 1 } -> { 0 } -> NULL', 4)
#     assert actual == expected



#########################
## These tests developed for Code Challenge 05 before
## extending LinkedList##
########################
# def test_import():
#     """ proof of life test passes"""
#     assert LinkedList
#     assert Node

# # initiate and empty list -- passes
# def test_new_empty():
#     empty_list = LinkedList()
#     actual = empty_list.head
#     expected = None
#     assert actual == expected

# # insert into linked list and 
# # head properly points to first node in list -- both pass
# def test_insert(generate_new_list):
#     generate_new_list.insert(17)
#     actual = generate_new_list.head.value
#     expected = 17
#     assert actual == expected
    
# # returns true when value in list is found -- passes
# def test_includes(generate_new_list):
#     actual = generate_new_list.includes(4)
#     expected = True
#     assert actual == expected
    
# # # returns false when value not in list -- passes
# def test_includes_not_found(generate_new_list):
#     actual = generate_new_list.includes(7)
#     expected = False
#     assert actual == expected

# # returns collection all values in list -- passes 
# # but not entirely sure why it's backwards
# def test_insert_many(generate_new_list):
#     actual = generate_new_list.insert_many()
#     expected = [4,3,2,1]
#     assert actual == expected
    


# ###### Fixture for CC05 ##########    
# @pytest.fixture
# def generate_new_list():
#     node = Node(0)
#     new_list = LinkedList(node)
#     list_length = 0
    
#     for value in range(1,5):
#         new_list.insert(value)
#         list_length += 1
    
#     return new_list
