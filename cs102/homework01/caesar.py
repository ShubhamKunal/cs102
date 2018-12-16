''' This is Caesar's Cipher'''


def encrypt_caesar(temp: str, key=3) -> str:
    """
    Encrypts plaintext using a_1 Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    from collections import deque
    albets = deque(list("abcdefghijklmnopqrstuvwxyz"))
    albets2 = deque(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    for counter in range(key):
        tempChar_1 = albets.popleft()
        tempChar_2 = albets2.popleft()
        albets.append(tempChar_1)
        albets2.append(tempChar_2)
    str1 = temp
    out_string = ""
    for temp_char in str1:
        if 'z' >= temp_char >= 'a':
            out_string += (albets[ord(temp_char)-97])
        elif 'A' <= temp_char <= 'Z':
            out_string += (albets2[ord(temp_char)-65])
        else:
            out_string += temp_char
    return out_string


def decrypt_caesar(temp: str, key=3) -> str:
    """
    Decrypts a_1 ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    from collections import deque
    albets = deque(list("abcdefghijklmnopqrstuvwxyz"))
    albets2 = deque(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    albets3 = deque(list("abcdefghijklmnopqrstuvwxyz"))
    albets4 = deque(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    for counter in range(key):
        tempChar_1 = albets.popleft()
        tempChar_2 = albets2.popleft()
        albets.append(tempChar_1)
        albets2.append(tempChar_2)
    str1 = temp
    out_string = ""
    for temp_char in str1:
        if 'z' >= temp_char >= 'a':
            out_string += albets3[list(albets).index(temp_char)]
        elif 'A' <= temp_char <= 'Z':
            out_string += albets4[list(albets2).index(temp_char)]
        else:
            out_string += temp_char
    return out_string
