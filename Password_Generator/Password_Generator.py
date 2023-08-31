import random
import string
def generate_password(length: int):
    if length < 8 or length > 20:
        raise ValueError("Password length should be between 8 and 20 characters")

    # Define character sets for different types of characters
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # generation of randon password
    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password

try:
    length = int(input("Enter the desired password length: "))
    password = generate_password(length)
    print("Generated Password: ", password)
except ValueError as e:
    print(e)


# Purpoe of raise ValueError: What will happen if we just write print and print the error message - 
  
# If you replace the line raise ValueError("Password length should be between 8 and 20 characters") with a print statement, the behavior of the code will change. Instead of raising an exception and stopping the program execution, the code will continue running normally after printing the error message. This means that if the user enters a password length that is outside the valid range (less than 8 or greater than 20), the error message will be printed, but the program will still proceed to generate a password using the provided length, even if it's invalid.
#In other words, if you use a print statement instead of the raise statement, there won't be any enforcement of the password length constraint, and passwords of any length will be generated regardless of whether they fall within the said valid range or not.
