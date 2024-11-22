import hashlib

# Function to compute SHA-256 hash of a password
def sha256_hash(password):
    # Create a new sha256 hash object
    sha256_hash = hashlib.sha256()
    
    # Update the hash object with the password encoded to bytes
    sha256_hash.update(password.encode('utf-8'))
    
    # Return the hexadecimal representation of the hash
    return sha256_hash.hexdigest()

# Example usage with user input
if __name__ == "__main__":
    # Get the password input from the user
    password = input("Enter your password: ")

    # Get the SHA-256 hash of the password
    hashed_password = sha256_hash(password)

    # Print the hashed password
    print(f"SHA-256 Hash: {hashed_password}")
