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

def test_single_character():
    assert is_palindrome("a")
    assert is_palindrome("A")
    assert is_palindrome(" ")

def test_special_characters():
    assert is_palindrome("$%*([])")
    assert is_palindrome("Madam, in Eden, I'm Adam")
    assert is_palindrome("No lemon, no melon!")

def test_numbers():
    assert is_palindrome("12321")
    assert not is_palindrome("12345")

def test_long_palindrome():
    long_palindrome = "a" * 10000 + "b" + "a" * 5000
    assert not is_palindrome(long_palindrome)

    long_palindrome = "a" * 10000 + "a" * 10000
    assert is_palindrome(long_palindrome)

def test_unicode():
    assert is_palindrome("😊a😊")
    assert not is_palindrome("a😊b😊")