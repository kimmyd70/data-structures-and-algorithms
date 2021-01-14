import pytest
from stacks_and_queues.stacks_and_queues import Stack, InvalidOperationError

# 
# Can successfully instantiate an empty queue
# Can successfully enqueue into a queue
def test_push_onto_empty():
    s = Stack()
    s.push("apple")
    actual = s.top.value
    expected = "apple"
    assert actual == expected

# 
# Can successfully enqueue multiple values into a queue
def test_push_onto_full():
    s = Stack()
    s.push("apple")
    s.push("banana")
    s.push("cucumber")
    actual = s.top.value
    expected = "cucumber"
    assert actual == expected

# 
# Can successfully dequeue out of a queue the expected value
def test_pop_single():
    s = Stack()
    s.push("apple")
    actual = s.pop()
    expected = "apple"
    assert actual == expected

# passes
def test_pop_some():
    s = Stack()

    s.push("apple")
    s.push("banana")
    s.push("cucumber")

    s.pop()

    actual = s.pop()
    expected = "banana"

    assert actual == expected

#passes
def test_check_not_empty():
    s = Stack()
    s.push("apple")
    s.push("banana")
    actual = s.is_empty()
    expected = False
    assert actual == expected

#   
# Can successfully empty a queue after multiple dequeues
def test_pop_until_empty():
    s = Stack()
    s.push("apple")
    s.push("banana")
    s.push("cucumber")
    s.pop()
    s.pop()
    s.pop()
    actual = s.is_empty()
    expected = True
    assert actual == expected

# 
# Can successfully peek into a queue, seeing the expected value
def test_peek():
    s = Stack()
    s.push("apple")
    s.push("banana")
    actual = s.peek()
    expected = "banana"
    assert actual == expected

# 
# Calling dequeue or peek on empty queue raises exception
def test_peek_empty():
    s = Stack()
    with pytest.raises(InvalidOperationError) as e:
        s.peek()

    assert str(e.value) == "Not allowed on empty structure"

#
# Calling dequeue or peek on empty queue raises exception
def test_pop_empty():
    s = Stack()
    with pytest.raises(InvalidOperationError) as e:
        s.pop()

    assert str(e.value) == "Not allowed on empty structure"