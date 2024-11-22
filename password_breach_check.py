import hashlib
import requests
import csv

# Function to check if the password is part of a data breach using "Have I Been Pwned" API
def check_password_breach(password):
    # Compute the SHA-1 hash of the password
    sha1_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    
    # Send the first 5 characters to the API
    first_five = sha1_hash[:5]
    remaining_hash = sha1_hash[5:]
    
    # Send GET request to the API with the first 5 characters of the hash
    url = f"https://api.pwnedpasswords.com/range/{first_five}"
    response = requests.get(url)
    
    # Check if the remaining hash is in the response
    if response.status_code == 200:
        if remaining_hash in response.text:
            return True  # Password found in breach
        else:
            return False  # Password not found in breach
    else:
        print("Error fetching data from Have I Been Pwned API")
        return None

# Function to check usernames and passwords from a file
def check_file_for_breaches(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        
        for row in reader:
            username, password = row
            
            # Check the password against the API
            print(f"Checking password for {username}...")
            if check_password_breach(password):
                print(f"Password for {username} has been pwned!")
            else:
                print(f"Password for {username} has NOT been pwned.")

# Example usage with user input
if __name__ == "__main__":
    # Path to the file containing usernames and passwords (use the file created earlier)
    file_path = "dummy_user_passwords.csv"
    
    # Check each username and password pair for data breaches
    check_file_for_breaches(file_path)
