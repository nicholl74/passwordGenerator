import random
import string


def generate_password(min_length, numbers=True, special_char=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    #  print(letters, digits, special)
    characters = letters
    if numbers:
        characters += digits
    if special_char:
        characters += special

    #  print(characters)

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_char:
            meets_criteria = has_special and meets_criteria

    return pwd


min_length = int(input("Enter minimum password length?"))
nums = input("Do you want to include digits? Y/N") .lower() == "y"
special = input("Do you want to include special characters?").lower() == "y"

password = generate_password(min_length, nums, special)

print(f"Here is your new password {password}")
