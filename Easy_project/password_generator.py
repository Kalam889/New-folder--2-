#PASSWORD GENERATOR

# import string
# import random 

# length = int(input("Enter length of password: "))
# letters = string.ascii_letters
# numbers = string.digits
# symbols = string.punctuation

# print("Password should contain:-")
# print("1. Numbers & Symbols")
# print("2. Only Letters ")
# print("3. All")
# choice = input("Enter your choice")
# if choice == "1":
#     password = ''.join(random.choice(numbers + symbols)for i in range(length))
#     print(password)
# elif choice == "2":
#     password = ''.join(random.choice(letters)for i in range(length))
#     print(password)
# elif choice == "3":
#     password =''.join( random.choice(letters+symbols+numbers)for i in range(length))
#     print(password)

# --------------------------------------------
#Upgrading to yes/no input option.

# import string
# import random

# length = int(input("Enter password length: "))

# letters = string.ascii_letters
# numbers = string.digits
# symbols = string.punctuation

# print("\nYour password should include:")
# use_letters = input("Include letters? (yes/no): ").lower()
# use_symbols = input("Include symbols? (yes/no): ").lower()
# use_numbers = input("Include numbers? (yes/no): ").lower()

# characters = ""

# if use_letters == "yes":
#     characters += letters
# if use_symbols == "yes":
#     characters += symbols
# if use_numbers == "yes":
#     characters += numbers

# if characters == "":
#     print("\nYou must select at least one option (letters, numbers, or symbols).")
# else:
#     password = ''.join(random.choice(characters) for _ in range(length))
#     print("\nYour generated password:", password)

# ----------------------------------------------------
#Upgrading to password strength.

import string
import random

length = int(input("Enter password length: "))
if length < 8:
    print("Password is too weak.")
elif length >= 8 and length < 12:
    print("Password is medium")
elif length >= 12 :
    print("Password is strong")
letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

print("\nYour password should include:")
use_letters = input("Include letters? (yes/no): ").lower()
use_symbols = input("Include symbols? (yes/no): ").lower()
use_numbers = input("Include numbers? (yes/no): ").lower()

characters = ""

if use_letters == "yes":
    characters += letters
if use_symbols == "yes":
    characters += symbols
if use_numbers == "yes":
    characters += numbers

if characters == "":
    print("\nYou must select at least one option (letters, numbers, or symbols).")
else:
    password = ''.join(random.choice(characters) for _ in range(length))
    print("\nYour generated password:", password)

    
# -----------------------------------------------------------------------------------------