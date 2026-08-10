import random
import string

# Generate password
def generate_password(length):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"

    password = ""

    for i in range(length):
        password += random.choice(characters)

    return password


# Main program
length = int(input("Enter password length: "))

password = generate_password(length)

print("Generated Password:", password)
