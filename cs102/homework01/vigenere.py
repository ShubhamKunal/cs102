''' Vigenere Cipher '''


def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    albets_string = "abcdefghijklmnopqrstuvwxyz"
    albets = list(albets_string)
    albets2 = list(albets_string.upper())
    ciphertext = ""
    keyword = keyword.lower()
    temp_num = 0
    for temp_char in plaintext:
        if 'a' <= temp_char <= 'z':
            code = albets.index(temp_char) + albets.index(keyword[temp_num % len(keyword)])
            code = code % 26
            ciphertext += albets[code]
        elif 'A' <= temp_char <= 'Z':
            code = albets2.index(temp_char) + albets.index(keyword[temp_num % len(keyword)])
            code = code % 26
            ciphertext += albets2[code]
        else:
            ciphertext += temp_char
        temp_num += 1
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:

    """
    Decrypts a_1 ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    albets_string = "abcdefghijklmnopqrstuvwxyz"
    albets = list(albets_string)
    albets2 = list(albets_string.upper())
    plaintext = ""
    temp_num = 0
    keyword = keyword.lower()
    for temp_char in ciphertext:
        if 'a' <= temp_char <= 'z':
            code = albets.index(temp_char) - albets.index(keyword[temp_num % len(keyword)])
            if code < 0:
                code = 26 + code
            plaintext += albets[code]
        elif 'A' <= temp_char <= 'Z':

            code = albets2.index(temp_char) - albets.index(keyword[temp_num % len(keyword)])
            if code < 0:
                code = code + 26
            plaintext += albets2[code]
        else:
            plaintext += temp_char
        temp_num += 1

    return plaintext
