import random
import string

def generate_password(length=12):
    # Generates a random password with letters, numbers, and symbols
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

# Generate and print a random password
print("Your password:", generate_password())
