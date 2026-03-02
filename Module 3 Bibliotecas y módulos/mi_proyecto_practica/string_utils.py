def count_vowels(text):
    """Cuenta y retorna el numero de vocales de un argumento String"""
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count