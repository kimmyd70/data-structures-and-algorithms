import pytest
from stacks_and_queues.stacks_and_queues import Queue, InvalidOperationError

# passes
# Can successfully enqueue into a queue
def test_enqueue_onto_empty():
    q = Queue()
    q.enqueue("apple")
    actual = q.front.value
    expected = "apple"
    assert actual == expected

# passes
# Can successfully enqueue multiple values into a queue
def test_enqueue_onto_full():
    q = Queue()
    q.enqueue("apple")
    q.enqueue("banana")
    q.enqueue("cucumber")
    actual = q.front.value
    expected = "apple"
    assert actual == expected

# passes
# Can successfully dequeue out of a queue the expected value
def test_dequeue_single():
    q = Queue()
    q.enqueue("apple")
    actual = q.dequeue()
    expected = "apple"
    assert actual == expected


#passes
def test_check_not_empty():
    q = Queue()
    q.enqueue("apple")
    q.enqueue("banana")
    actual = q.q_is_empty()
    expected = False
    assert actual == expected

# passes
# Can successfully empty a queue after multiple dequeues
def test_dequeue_until_empty():
    q = Queue()
    q.enqueue("apple")
    q.enqueue("banana")
    q.enqueue("cucumber")
    q.dequeue()
    q.dequeue()
    q.dequeue()
    actual = q.q_is_empty()
    expected = True
    assert actual == expected

# 
# Can successfully peek into a queue, seeing the expected value
def test_q_peek():
    q = Queue()
    q.enqueue("apple")
    q.enqueue("banana")
    actual = q.q_peek()
    expected = "apple"
    assert actual == expected

# passes
# Calling dequeue or peek on empty queue raises exception
def test_peek_empty():
    q = Queue()
    with pytest.raises(InvalidOperationError) as e:
        q.q_peek()

    assert str(e.value) == "Not allowed on empty structure"

# passes
# Calling dequeue or peek on empty queue raises exception
def test_dequeue_empty():
    q = Queue()
    with pytest.raises(InvalidOperationError) as e:
        q.dequeue()

    assert str(e.value) == "Not allowed on empty structure"