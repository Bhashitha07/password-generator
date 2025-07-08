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

    length = int(input("Enter password length (e.g. 12): "))
    use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    password = generate_password(length, use_upper, use_digits, use_symbols)
    print(f"\nGenerated Password: {password}")
