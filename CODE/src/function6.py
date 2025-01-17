def count_vowels(s):
    """Conta o número de vogais em uma string."""
    return sum(1 for char in s.lower() if char in "aeiou")