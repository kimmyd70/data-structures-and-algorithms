import pytest
from multi_bracket_validation import *

def test_import():
    """ proof of life test passes"""
    assert bracket_check
    
#
def test_empty_string():
    actual = bracket_check('')
    expected = True
    assert actual == expected
