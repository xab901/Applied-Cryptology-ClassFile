import string
import random


def generate_cipher_table():
    """
    Generates a random substitution table for single table cipher.
    
    Returns:
        dict: A mapping of plaintext letters to ciphertext letters.
    """
    alphabet = string.ascii_lowercase  # Generate the alphabet
    shuffled = list(alphabet)
    random.shuffle(shuffled)  # Randomly shuffle the alphabet
    return dict(zip(alphabet, shuffled))


def encrypt_single_table_cipher_with_table(plaintext, cipher_table):
    """
    Encrypts the plaintext using a substitution cipher based on a cipher table.
    
    Parameters:
        plaintext (str): The text to be encrypted.
        cipher_table (dict): The substitution cipher table.
    
    Returns:
        str: The encrypted ciphertext.
    """
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            is_upper = char.isupper()
            mapped_char = cipher_table[char.lower()]  # Map lowercase character
            ciphertext += mapped_char.upper() if is_upper else mapped_char
        else:
            ciphertext += char  # Non-alphabetic characters remain unchanged
    return ciphertext


def decrypt_single_table_cipher_with_table(ciphertext, cipher_table):
    """
    Decrypts the ciphertext using a substitution cipher based on a cipher table.
    
    Parameters:
        ciphertext (str): The text to be decrypted.
        cipher_table (dict): The substitution cipher table.
    
    Returns:
        str: The decrypted plaintext.
    """
    reverse_table = {v: k for k, v in cipher_table.items()}  # Reverse the cipher table
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            is_upper = char.isupper()
            mapped_char = reverse_table[char.lower()]  # Map using reverse table
            plaintext += mapped_char.upper() if is_upper else mapped_char
        else:
            plaintext += char  # Non-alphabetic characters remain unchanged
    return plaintext


# Example usage
if __name__ == "__main__":
    # User input
    plaintext = input("Enter the plaintext: ")

    # Generate cipher table
    cipher_table = generate_cipher_table()
    print("Cipher Table:", cipher_table)

    # Encrypt the plaintext
    encrypted_text = encrypt_single_table_cipher_with_table(plaintext, cipher_table)
    print("Encrypted Text:", encrypted_text)

    # Decrypt the ciphertext
    decrypted_text = decrypt_single_table_cipher_with_table(encrypted_text, cipher_table)
    print("Decrypted Text:", decrypted_text)