from hashtable import Hashtable
import pytest

##### tests from Roger's demo ######
@pytest.mark.skip("passed on previous run")
def test_create():
    hashtable = Hashtable()
    assert hashtable

@pytest.mark.skip("passed on previous run")
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

@pytest.fixture
def test_table():
    hashtable = Hashtable()
    hashtable.set("age", 23)
    hashtable.set("letters", "abc")
    hashtable.set("yellow", "banana")
    return hashtable


# @pytest.mark.skip("passed on previous run")
def test_set():
    hashtable = Hashtable()
    hashtable.set("number", 17)
    actual = hashtable.get("number")
    expected = 17
    assert actual == expected


# @pytest.mark.skip("passed on previous run")
def test_set_fail():
    hashtable = Hashtable()
    hashtable.set("number", 17)
    actual = hashtable.get("fail")
    expected = 23
    assert actual != expected


# @pytest.mark.skip("passed on previous run")
def test_get1(test_table):
    actual = test_table.get("yellow")
    expected = "banana"
    assert actual == expected


# @pytest.mark.skip("passed on previous run")
def test_get2(test_table):
    actual = test_table.get("letters")
    expected = "abc"
    assert actual == expected


# @pytest.mark.skip("passed on previous run")
def test_get_fail(test_table):
    actual = test_table.get("yellow")
    expected = "apple"
    assert actual != expected


# @pytest.mark.skip("passed on previous run")
def test_contains_true(test_table):
    actual = test_table.contains("yellow")
    expected = True
    assert actual == expected


# @pytest.mark.skip("passed on previous run")
def test_contains_false(test_table):
    actual = test_table.contains("name")
    expected = False
    assert actual == expected


# @pytest.mark.skip("pending")
def test_contains_fail(test_table):
    actual = test_table.contains("name")
    expected = True
    assert actual != expected