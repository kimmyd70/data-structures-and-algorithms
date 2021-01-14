import pytest
from queues_with_stacks import PseudoQueue, InvalidOperationError, Node, Stack

def test_import():
    """ proof of life test passes"""
    assert PseudoQueue
    assert Node
    assert Stack
    assert InvalidOperationError
