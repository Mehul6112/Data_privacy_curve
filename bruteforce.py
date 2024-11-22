import itertools
import string
import time

# Function to perform brute-force attack
def brute_force_attack(target_password):
    # Define the character set to use for the attack
    charset = string.ascii_letters + string.digits + string.punctuation
    
    # Start timer to measure attack time
    start_time = time.time()
    
    # Iterate over all possible lengths
    for length in range(1, len(target_password) + 1):
        # Generate all combinations of the given length
        for attempt in itertools.product(charset, repeat=length):
            # Convert tuple to string
            attempt_password = ''.join(attempt)
            
            # Check if the generated password matches the target
            if attempt_password == target_password:
                elapsed_time = time.time() - start_time
                print(f"Password found: {attempt_password}")
                print(f"Time taken: {elapsed_time:.2f} seconds")
                return
    
    # If no match found
    print("Password not found.")

# Example usage
if __name__ == "__main__":
    # Take the target password as user input
    target_password = input("Enter the password to simulate brute-force attack: ")
    
    print("Starting brute-force attack...")
    brute_force_attack(target_password)
