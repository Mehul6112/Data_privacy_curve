# Function to encrypt the plaintext
def encrypt(plaintext, shift):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            # Shift the character and ensure it's within the alphabet
            shift_base = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            # Non-alphabetic characters are added unchanged
            encrypted_text += char
    return encrypted_text

# Function to decrypt the ciphertext
def decrypt(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            # Reverse the shift to decrypt
            shift_base = 65 if char.isupper() else 97
            decrypted_text += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            # Non-alphabetic characters are added unchanged
            decrypted_text += char
    return decrypted_text

# Example usage with user input
if __name__ == "__main__":
    # Get user input
    plaintext = input("Enter the text to encrypt: ")
    shift = int(input("Enter the shift value (integer): "))

    # Encrypt the input text
    encrypted = encrypt(plaintext, shift)
    print(f"Encrypted Text: {encrypted}")

    # Decrypt the text back
    decrypted = decrypt(encrypted, shift)
    print(f"Decrypted Text: {decrypted}")
