import unittest
from palindrome import is_palindrome

class TestPalindrome(unittest.TestCase):
    def test_basic_palindromes(self):
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome(""))

    def test_non_palindromes(self):
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("world"))

    def test_case_insensitivity(self):
        self.assertTrue(is_palindrome("Madam"))
        self.assertTrue(is_palindrome("RaceCar"))

    def test_spaces(self):
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))
        self.assertFalse(is_palindrome("This is not a palindrome"))

if __name__ == '__main__':
    unittest.main()