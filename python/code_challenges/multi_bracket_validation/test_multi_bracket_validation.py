import pytest
from multi_bracket_validation import *

def test_import():
    """ proof of life test passes"""
    assert bracket_check
    
# passes
def test_empty_string():
    actual = bracket_check('')
    expected = True
    assert actual == expected

#passes
def test_basic_string():
    actual = bracket_check('()[]{}')
    expected = True
    assert actual == expected
    
# passes
def test_balanced_string():
    actual = bracket_check('(aslj(l;al))[yes]')
    expected = True
    assert actual == expected
    
#passes
def test_unbalanced_string():
    actual = bracket_check('(wrpu{al;j}')
    expected = False
    assert actual == expected