def find_max(numbers):
    """Encontra o maior número em uma lista."""
    if not numbers:
        raise ValueError("Lista não pode estar vazia.")
    return max(numbers)