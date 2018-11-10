''' Vigenere Cipher '''


def encrypt_vigenere(plaintext, keyword):
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
    n_1 = 0
    for a_1 in plaintext:
        if 'a' <= a_1 <= 'z':
            code = albets.index(a_1) + albets.index(keyword[n_1 % len(keyword)])
            code = code % 26
            ciphertext += albets[code]
        elif 'A' <= a_1 <= 'Z':
            code = albets2.index(a_1) + albets.index(keyword[n_1 % len(keyword)])
            code = code % 26
            ciphertext += albets2[code]
        else:
            ciphertext += a_1
        n_1 += 1
    return ciphertext


def decrypt_vigenere(ciphertext, keyword):

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
    n_1 = 0
    keyword = keyword.lower()
    for a_1 in ciphertext:
        if 'a' <= a_1 <= 'z':
            code = albets.index(a_1) - albets.index(keyword[n_1 % len(keyword)])
            if code < 0:
                code = 26 + code
            plaintext += albets[code]
        elif 'A' <= a_1 <= 'Z':

            code = albets2.index(a_1) - albets.index(keyword[n_1 % len(keyword)])
            if code < 0:
                code = code + 26
            plaintext += albets2[code]
        else:
            plaintext += a_1
        n_1 += 1

    return plaintext
