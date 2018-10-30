

def encrypt_caesar(temp,key=3):
    """
    Encrypts plaintext using a Caesar cipher.

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
    albets=deque(list("abcdefghijklmnopqrstuvwxyz"))
    albets2=deque(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    albets3=deque(list("abcdefghijklmnopqrstuvwxyz"))
    albets4=deque(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

    for a in range(key):
        t=albets.popleft()
        t2=albets2.popleft()
        albets.append(t)
        albets2.append(t2)
    str1 = temp

    out_string=""
    for a in str1:
        if('z'>=a>='a'):
            out_string+=(albets[ord(a)-97])
        elif('A'<=a<='Z'):
            out_string+=(albets2[ord(a)-65])
        else:
            out_string+=a
    return out_string

def decrypt_caesar(temp,key=3):
    """
    Decrypts a ciphertext using a Caesar cipher.

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
    albets=deque(list("abcdefghijklmnopqrstuvwxyz"))
    albets2=deque(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    albets3=deque(list("abcdefghijklmnopqrstuvwxyz"))
    albets4=deque(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

    for a in range(key):
        t=albets.popleft()
        t2=albets2.popleft()
        albets.append(t)
        albets2.append(t2)

    str1=temp
    out_string=""
    for a in str1:
        if(122>=ord(a)>=97):
            out_string+=albets3[albets.index(a)]
        elif(65<=ord(a)<=90):
            out_string+=albets4[albets2.index(a)]
        else:
            out_string+=a

    return out_string


