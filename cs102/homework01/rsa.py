''' RSA Encryption'''
import random
import math


def is_prime(inp_num: int) -> bool:
    """
    >>> is_prime(2)
    True
    >>> is_prime(11)
    True
    >>> is_prime(8)
    False
    """
    if inp_num == 2:
        return True
    if inp_num % 2 == 0 or inp_num <= 1:
        return False
    sqr = int(math.sqrt(inp_num)) + 1

    for divisor in range(3, sqr, 2):
        if inp_num % divisor == 0:
            return False
    return True


def gcd(input_1: int, input_2: int) -> int:
    """
    >>> gcd(12, 15)
    3
    >>> gcd(3, 7)
    1
    """
    if input_2 == 0:
        return input_1
    return gcd(input_2, input_1 % input_2)


def egcd(input_1: int, input_2: int) -> int:
    ''' To calculate Extended great common divisor'''
    if input_1 == 0:
        return (input_2, 0, 1)
    param1, param2, param3 = egcd(input_2 % input_1, input_1)
    return (param1, param3 - (input_2 // input_1) * param2, param2)


def multiplicative_inverse(input1: int, phi: int) -> int:
    """
    >>> multiplicative_inverse(7, 40)
    23
    """
    param1, param2, param3 = egcd(input1, phi)
    if param1 != 1:
        raise Exception('modular inverse does not exist')
    else:
        return param2 % phi


def generate_keypair(p: int, q: int) -> tuple:
    ''' To generate keypair '''
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')
    n = p*q
    # PUT YOUR CODE HERE
    phi = (p-1)*(q-1)
    # PUT YOUR CODE HERE
    # Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)
    # Use Euclid's Algorithm to verify that e and phi(n) are comprime
    g = gcd(e_1, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)
    # Use Extended Euclid's Algorithm to generate the private key
    d = multiplicative_inverse(e, phi)
    # Return public and private keypair
    # Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))


def encrypt(pk: int, plaintext: str) -> str:
    ''' Function to encrypt the text'''
    # Unpack the key into it's components
    key, n = pk
    # Convert each letter in the plaintext to numbers based on
    # the character using a^b mod m
    cipher = [(ord(char) ** key) % n for char in plaintext]
    # Return the array of bytes
    return cipher


def decrypt(pk: int, ciphertext: str) -> str:
    '''Function to decrypt the text '''
    # Unpack the key into its components
    key, n = pk
    # Generate the plaintext based on the ciphertext and key using a^b mod m
    plain = [chr((int(char ** key)) % n) for char in ciphertext]
    # Return the array of bytes as a string
    return ''.join(plain)


if __name__ == '__main__':
    print ("RSA Encrypter/ Decrypter)")
    P = int(input("Enter a prime number (17, 19, 23, etc): "))
    Q = int(input("Enter another prime number: "))
    print("Generating your public/private keypairs now . . .")
    PUBLIC, PRIVATE = generate_keypair(P, Q)
    print("Your public key is ", PUBLIC, " and your private key is ", PRIVATE)
    MESSAGE = input("Enter a message to encrypt with your private key: ")
    ENCRYPTED_MSG = encrypt(PRIVATE, MESSAGE)
    print("Your encrypted message is: ")
    print(ENCRYPTED_MSG)
    print("Decrypting message with public key ", PUBLIC, " . . .")
    print("Your message is:")
    print(decrypt(PUBLIC, ENCRYPTED_MSG))
