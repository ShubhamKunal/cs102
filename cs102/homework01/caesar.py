''' This is Caesar's Cipher'''


def encrypt_caesar(temp, key=3):
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
    for a_1 in range(key):
        t_1 = albets.popleft()
        t_2 = albets2.popleft()
        albets.append(t_1)
        albets2.append(t_2)
    str1 = temp
    out_string = ""
    for a_1 in str1:
        if 'z' >= a_1 >= 'a':
            out_string += (albets[ord(a_1)-97])
        elif 'A' <= a_1 <= 'Z':
            out_string += (albets2[ord(a_1)-65])
        else:
            out_string += a_1
    return out_string


def decrypt_caesar(temp, key=3):
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
    for a_1 in range(key):
        t_1 = albets.popleft()
        t_2 = albets2.popleft()
        albets.append(t_1)
        albets2.append(t_2)
    str1 = temp
    out_string = ""
    for a_1 in str1:
        if 'z' >= a_1 >= 'a':
            out_string += albets3[list(albets).index(a_1)]
        elif 'A' <= a_1 <= 'Z':
            out_string += albets4[list(albets2).index(a_1)]
        else:
            out_string += a_1
    return out_string
