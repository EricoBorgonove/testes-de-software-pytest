def is_palindrome(s):
    """Verifica se uma string é um palíndromo."""
    s = s.lower().replace(" ", "")
    return s == s[::-1]
