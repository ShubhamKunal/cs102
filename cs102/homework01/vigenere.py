
def encrypt_vigenere(plaintext, keyword):
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    albets_string="abcdefghijklmnopqrstuvwxyz"
    albets=list(albets_string)
    albets2=list(albets_string.upper())
    ciphertext = ""
    keyword=keyword.lower()
    n=0
    for a in plaintext:
        if('a'<=a<='z'):
            code= albets.index(a)+albets.index(keyword[n%len(keyword)])
            code=(code%26)
            
            ciphertext+=albets[code]
        elif('A'<=a<='Z'):
            code= albets2.index(a)+albets.index(keyword[n%len(keyword)])
            code=code%26
            ciphertext+=albets2[code]
        else:
            ciphertext+=a
        n+=1
       




    return ciphertext
        
def decrypt_vigenere(ciphertext, keyword):

    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    albets_string="abcdefghijklmnopqrstuvwxyz"
    albets=list(albets_string)
    albets2=list(albets_string.upper())
    plaintext=""
    n=0
    keyword=keyword.lower()
    for a in ciphertext:
        
        if('a'<=a<='z'):
            code= albets.index(a)-albets.index(keyword[n%len(keyword)])
            if code<0:
                code=26+code
            plaintext+=albets[code]
        elif('A'<=a<='Z'):

            code= albets2.index(a)-albets.index(keyword[n%len(keyword)])
            if(code<0):
                code=code+26
            plaintext+=albets2[code]
        else:
            plaintext+=a
        n+=1


    return plaintext


