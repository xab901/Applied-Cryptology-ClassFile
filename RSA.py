import random
from sympy import isprime, nextprime
from math import gcd
from functools import reduce

# Function to generate a random prime number with N bits
def generate_large_prime(N: int) -> int:
    # Generate a random odd number with N bits
    candidate = random.getrandbits(N) | 1
    # Find the next prime number from the candidate
    prime = nextprime(candidate)
    return prime

# Function to compute modular inverse using Extended Euclidean Algorithm
def modular_inverse(a: int, m: int) -> int:
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

# RSA key generation
def rsa_key_generation(N: int):
    # Step 1: Generate two large primes, p and q
    p = generate_large_prime(N)
    q = generate_large_prime(N)
    while p == q:  # Ensure p and q are distinct
        q = generate_large_prime(N)

    # Step 2: Compute n and φ(n)
    n = p * q
    phi_n = (p - 1) * (q - 1)

    # Step 3: Choose e such that 1 < e < φ(n) and gcd(e, φ(n)) = 1
    e = 65537  # Commonly used value for e
    if gcd(e, phi_n) != 1:
        e = nextprime(65537)

    # Step 4: Compute d, the modular multiplicative inverse of e modulo φ(n)
    d = modular_inverse(e, phi_n)

    return (e, n), (d, n)

# RSA encryption
def rsa_encrypt(public_key: tuple, plaintext: int) -> int:
    e, n = public_key
    return pow(plaintext, e, n)

# RSA decryption
def rsa_decrypt(private_key: tuple, ciphertext: int) -> int:
    d, n = private_key
    return pow(ciphertext, d, n)

# Example usage
if __name__ == "__main__":
    N = 16  # Bit size of the primes
    plaintext = 42  # Message to encrypt (must be less than n)

    # Generate RSA keys
    public_key, private_key = rsa_key_generation(N)
    print(f"Public Key: {public_key}")
    print(f"Private Key: {private_key}")

    # Encrypt the message
    ciphertext = rsa_encrypt(public_key, plaintext)
    print(f"Ciphertext: {ciphertext}")

    # Decrypt the message
    decrypted_message = rsa_decrypt(private_key, ciphertext)
    print(f"Decrypted Message: {decrypted_message}")