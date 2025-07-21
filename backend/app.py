import random
import string

def generate_password(length=12, use_upper=True, use_digits=True, use_symbols=True):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if use_upper else ''
    digits = string.digits if use_digits else ''
    symbols = string.punctuation if use_symbols else ''

    all_chars = lowercase + uppercase + digits + symbols

    if not all_chars:
        return "Error: No character sets selected!"

    password = []
    if use_upper:
        password.append(random.choice(uppercase))
    if use_digits:
        password.append(random.choice(digits))
    if use_symbols:
        password.append(random.choice(symbols))

    while len(password) < length:
        password.append(random.choice(all_chars))

    random.shuffle(password)
    return ''.join(password)

if __name__ == "__main__":
    print(" Password Generator ")

    while True:
        try:
            length = int(input("Enter password length (1-12): "))
            if length < 1 or length > 12:
                raise ValueError("Password length must be between 1 and 12.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter an integer between 1 and 12.")

    use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    if not (use_upper or use_digits or use_symbols):
        print("Error: At least one character set must be selected!")
    else:
        password = generate_password(length, use_upper, use_digits, use_symbols)
        print(f"\nGenerated Password: {password}")
