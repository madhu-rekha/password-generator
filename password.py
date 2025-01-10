import random
import string

def generate_password(length=12, use_uppercase=True, use_numbers=True, use_special=True):
    """Generate a random password."""
    if length < 4:
        raise ValueError("Password length must be at least 4 characters.")
    
    # Define character pools
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if use_uppercase else ""
    numbers = string.digits if use_numbers else ""
    special = string.punctuation if use_special else ""
    
    # Combine character pools
    all_characters = lowercase + uppercase + numbers + special
    if not all_characters:
        raise ValueError("At least one character type must be selected.")
    
    # Ensure password contains at least one of each selected type
    password = [
        random.choice(lowercase),
        random.choice(uppercase) if use_uppercase else "",
        random.choice(numbers) if use_numbers else "",
        random.choice(special) if use_special else ""
    ]
    
    # Fill the rest of the password length
    password += random.choices(all_characters, k=length - len(password))
    random.shuffle(password)
    
    return "".join(password)

def save_password_to_file(password, filename="passwords.txt"):
    """Save the generated password to a file."""
    with open(filename, "a") as file:
        file.write(password + "\n")
    print(f"Password saved to {filename}.")

# Main function to run the program
def main():
    print("Random Password Generator")
    length = int(input("Enter the desired password length (minimum 4): "))
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'

    try:
        password = generate_password(length, use_uppercase, use_numbers, use_special)
        print(f"Generated Password: {password}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
