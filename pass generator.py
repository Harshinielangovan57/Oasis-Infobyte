import random
import string

def get_user_preferences():
    try:
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            raise ValueError("Password length must be greater than 0.")
    except ValueError as e:
        print(f"Invalid input: {e}")
        return get_user_preferences()

    include_letters = input("Include letters? (y/n): ").strip().lower() == 'y'
    include_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
    include_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'

    if not (include_letters or include_numbers or include_symbols):
        print("You must include at least one character type!")
        return get_user_preferences()

    return length, include_letters, include_numbers, include_symbols

# Function to generate a password based on user preferences
def generate_password(length, include_letters, include_numbers, include_symbols):
    character_pool = []
    if include_letters:
        character_pool.extend(string.ascii_letters)  # Add letters
    if include_numbers:
        character_pool.extend(string.digits)  # Add numbers
    if include_symbols:
        character_pool.extend(string.punctuation)  # Add symbols
    if not character_pool:
        raise ValueError("No character types selected!")
    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    length, include_letters, include_numbers, include_symbols = get_user_preferences()
    password = generate_password(length, include_letters, include_numbers, include_symbols)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()    
