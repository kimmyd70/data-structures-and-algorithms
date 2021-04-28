from hashtable import Hashtable
import pytest

##### tests from Roger's demo ######
@pytest.mark.skip("passed on previous run")
def test_create():
    hashtable = Hashtable()
    assert hashtable

# @pytest.mark.skip("passed on previous run")
def test_predictable_hash():
    hashtable = Hashtable()
    initial = hashtable._hash('spam')
    secondary = hashtable._hash('spam')
    assert initial == secondary


@pytest.mark.skip("passed on previous run")
def test_in_range_hash():
    hashtable = Hashtable()
    actual = hashtable._hash('spam')

    # assert actual >= 0
    # assert actual < hashtable._size

    assert 0 <= actual < hashtable._size


@pytest.mark.skip("passed on previous run")
def test_same_hash():
    hashtable = Hashtable()
    initial = hashtable._hash('listen')
    secondary = hashtable._hash('silent')
    assert initial == secondary


@pytest.mark.skip("passed on previous run")
def test_different_hash():
    hashtable = Hashtable()
    initial = hashtable._hash('glisten')
    secondary = hashtable._hash('silent')
    assert initial != secondary
    
###################################