# palindrome.py

def is_palindrome(s: str) -> bool:
    """
    Check if the given string is a palindrome.
    
    A palindrome is a word that reads the same backward as forward.
    """
    s = s.lower().replace(" ", "")
    return s == s[::-1]