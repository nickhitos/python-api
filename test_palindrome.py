# test_palindrome.py

from palindrome import is_palindrome

def test_basic_palindromes():
    assert is_palindrome("madam")
    assert is_palindrome("racecar")
    assert is_palindrome("")

def test_non_palindromes():
    assert not is_palindrome("hello")
    assert not is_palindrome("world")

def test_case_insensitivity():
    assert is_palindrome("Madam")
    assert is_palindrome("RaceCar")

def test_spaces():
    assert is_palindrome("A man a plan a canal Panama")
    assert not is_palindrome("This is not a palindrome")