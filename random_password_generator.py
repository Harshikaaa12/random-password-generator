import random
import string

print("=== Random Password Generator ===")

while True:
    while True:
        try:
            length = int(input("\nEnter password length (minimum 8): "))

            if length < 8:
                print("Password length must be at least 8.")
            else:
                break

        except ValueError:
            print("Please enter a valid number.")

    uppercase = input("Include uppercase letters? (y/n): ").lower() == "y"
    lowercase = input("Include lowercase letters? (y/n): ").lower() == "y"
    numbers = input("Include numbers? (y/n): ").lower() == "y"
    symbols = input("Include symbols? (y/n): ").lower() == "y"

    selected_types = sum([uppercase, lowercase, numbers, symbols])

    if selected_types < 2:
        print("\nError: Please select at least two character types.")
        continue

    character_pool = ""
    password_characters = []

    if uppercase:
        character_pool += string.ascii_uppercase
        password_characters.append(random.choice(string.ascii_uppercase))

    if lowercase:
        character_pool += string.ascii_lowercase
        password_characters.append(random.choice(string.ascii_lowercase))

    if numbers:
        character_pool += string.digits
        password_characters.append(random.choice(string.digits))

    if symbols:
        character_pool += string.punctuation
        password_characters.append(random.choice(string.punctuation))

    remaining_length = length - len(password_characters)

    for _ in range(remaining_length):
        password_characters.append(random.choice(character_pool))

    random.shuffle(password_characters)
    password = "".join(password_characters)

    print("\nYour generated password is:")
    print(password)

    again = input("\nGenerate another password? (y/n): ").lower()

    if again != "y":
        print("Thank you for using the Password Generator!")
        break