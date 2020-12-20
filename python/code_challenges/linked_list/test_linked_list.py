from linked_list import LinkedList, Node
import pytest


def test_import():
    """ proof of life test passes"""
    assert LinkedList
    assert Node

def test_node_init():
    """ """
    actual = __init__(2)
    expected = 2
    assert actual == expected
    