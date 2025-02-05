import pytest

from app import add

def test_empty_string():
    assert add("") == 0

def test_single_number():
    assert add("1") == 1

def test_two_numbers():
    assert add("1,2") == 3

def test_newline_delimiter():
    assert add("1\n2,3") == 6

def test_custom_delimiter():
    assert add("//;\n1;2") == 3