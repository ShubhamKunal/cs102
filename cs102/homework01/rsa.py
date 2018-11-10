''' RSA Encryption'''
import random
import math


def is_prime(n_1):
    """
    >>> is_prime(2)
    True
    >>> is_prime(11)
    True
    >>> is_prime(8)
    False
    """
    if n_1 == 2:
        return True
    if n_1 % 2 == 0 or n_1 <= 1:
        return False
    sqr = int(math.sqrt(n_1)) + 1

    for divisor in range(3, sqr, 2):
        if n_1 % divisor == 0:
            return False
    return True


def gcd(a_1, b_1):
    """
    >>> gcd(12, 15)
    3
    >>> gcd(3, 7)
    1
    """
    if b_1 == 0:
        return a_1
    return gcd(b_1, a_1 % b_1)


def egcd(a_1, b_1):
    ''' To calculate Extended great common divisor'''
    if a_1 == 0:
        return (b_1, 0, 1)
    g_1, y_1, x_1 = egcd(b_1 % a_1, a_1)
    return (g_1, x_1 - (b_1 // a_1) * y_1, y_1)


def multiplicative_inverse(e_1, phi):
    """
    >>> multiplicative_inverse(7, 40)
    23
    """
    g_1, x_1, y_1 = egcd(e_1, phi)
    if g_1 != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x_1 % phi


def generate_keypair(p_1, q_1):
    ''' To generate keypair '''
    if not (is_prime(p_1) and is_prime(q_1)):
        raise ValueError('Both numbers must be prime.')
    elif p_1 == q_1:
        raise ValueError('p and q cannot be equal')
    n_1 = p_1*q_1
    # PUT YOUR CODE HERE
    phi = (p_1-1)*(q_1-1)
    # PUT YOUR CODE HERE
    # Choose an integer e such that e and phi(n) are coprime
    e_1 = random.randrange(1, phi)
    # Use Euclid's Algorithm to verify that e and phi(n) are comprime
    g_1 = gcd(e_1, phi)
    while g_1 != 1:
        e_1 = random.randrange(1, phi)
        g_1 = gcd(e_1, phi)
    # Use Extended Euclid's Algorithm to generate the private key
    d_1 = multiplicative_inverse(e_1, phi)
    # Return public and private keypair
    # Public key is (e, n) and private key is (d, n)
    return ((e_1, n_1), (d_1, n_1))


def encrypt(pk_1, plaintext):
    ''' Function to encrypt the text'''
    # Unpack the key into it's components
    key, n_1 = pk_1
    # Convert each letter in the plaintext to numbers based on
    # the character using a^b mod m
    cipher = [(ord(char) ** key) % n_1 for char in plaintext]
    # Return the array of bytes
    return cipher


def decrypt(pk_1, ciphertext):
    '''Function to decrypt the text '''
    # Unpack the key into its components
    key, n_1 = pk_1
    # Generate the plaintext based on the ciphertext and key using a^b mod m
    plain = [chr((int(char ** key)) % n_1) for char in ciphertext]
    # Return the array of bytes as a string
    return ''.join(plain)


if __name__ == '__main__':
    print "RSA Encrypter/ Decrypter"
    P_1 = int(input("Enter a prime number (17, 19, 23, etc): "))
    Q_1 = int(input("Enter another prime number: "))
    print "Generating your public/private keypairs now . . ."
    PUBLIC, PRIVATE = generate_keypair(P_1, Q_1)
    print("Your public key is ", PUBLIC, " and your private key is ", PRIVATE)
    MESSAGE = input("Enter a message to encrypt with your private key: ")
    ENCRYPTED_MSG = encrypt(PRIVATE, MESSAGE)
    print "Your encrypted message is: "
    print ENCRYPTED_MSG
    print "Decrypting message with public key ", PUBLIC, " . . ."
    print "Your message is:"
    print decrypt(PUBLIC, ENCRYPTED_MSG)
