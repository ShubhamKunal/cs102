from collections import deque
albets=deque(list("abcdefghijklmnopqrstuvwxyz"))
albets2=deque(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
albets3=deque(list("abcdefghijklmnopqrstuvwxyz"))
albets4=deque(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
key=int(input("Enter the key (for doctesting enter 3): "))
for a in range(key):
    t=albets.popleft()
    t2=albets2.popleft()
    albets.append(t)
    albets2.append(t2)
def encrypt_caesar(temp):
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
    
    str1 = temp

    out_string=""
    for a in str1:
        if(122>=ord(a)>=97):
            out_string+=(albets[ord(a)-97])
        elif(65<=ord(a)<=90):
            out_string+=(albets2[ord(a)-65])
        else:
            out_string+=a
    return out_string

def decrypt_caesar(temp):
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


