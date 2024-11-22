# Function to encrypt the plaintext using Rail Fence Cipher
def encrypt(plaintext, rails):
    # Create a 2D list to represent the rail fence
    fence = [['' for _ in range(len(plaintext))] for _ in range(rails)]
    
    # Variables to keep track of the current position in the rails
    row, step = 0, 1
    
    # Fill the fence with the plaintext in a zigzag manner
    for col in range(len(plaintext)):
        fence[row][col] = plaintext[col]
        
        # Change direction when we reach the top or bottom rail
        if row == 0:
            step = 1
        elif row == rails - 1:
            step = -1
        
        row += step
    
    # Concatenate all rows to get the encrypted text
    encrypted_text = ''.join(''.join(row) for row in fence)
    return encrypted_text

# Function to decrypt the ciphertext using Rail Fence Cipher
def decrypt(ciphertext, rails):
    # Create a 2D list to represent the rail fence
    fence = [['' for _ in range(len(ciphertext))] for _ in range(rails)]
    
    # Variables to keep track of the current position in the rails
    row, step = 0, 1
    index = 0
    
    # First, place all characters from the ciphertext in the zigzag pattern
    for col in range(len(ciphertext)):
        fence[row][col] = '*'
        
        if row == 0:
            step = 1
        elif row == rails - 1:
            step = -1
        
        row += step
    
    # Fill the fence with the characters from the ciphertext
    for row in range(rails):
        for col in range(len(ciphertext)):
            if fence[row][col] == '*':
                fence[row][col] = ciphertext[index]
                index += 1
    
    # Read the message row by row
    decrypted_text = ''
    row, step = 0, 1
    for col in range(len(ciphertext)):
        decrypted_text += fence[row][col]
        
        if row == 0:
            step = 1
        elif row == rails - 1:
            step = -1
        
        row += step
    
    return decrypted_text

# Example usage with user input
if __name__ == "__main__":
    # Get user input
    plaintext = input("Enter the text to encrypt: ")
    rails = int(input("Enter the number of rails: "))

    # Encrypt the input text
    encrypted = encrypt(plaintext, rails)
    print(f"Encrypted Text: {encrypted}")

    # Decrypt the text back
    decrypted = decrypt(encrypted, rails)
    print(f"Decrypted Text: {decrypted}")
