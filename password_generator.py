import random

# Function to generate a strong password from the dictionary file
def generate_password(length, dictionary_file_path):
    # Open the dictionary file and load words
    with open(dictionary_file_path, mode="r") as file:
        words = [line.strip() for line in file]
    
    # Generate password by randomly selecting words from the dictionary
    password = random.sample(words, length)
    
    # Combine the words into a single password string
    return ''.join(password)

# Example usage:
if __name__ == "__main__":
    # Define the path to the dummy dictionary file
    dictionary_file_path = "dummy_dictionary.txt"  # Replace with the correct path on your system
    
    # Ask the user for password length
    password_length = int(input("Enter the number of words for the password: "))
    
    # Generate the password
    generated_password = generate_password(password_length, dictionary_file_path)
    print(f"Generated Password: {generated_password}")
