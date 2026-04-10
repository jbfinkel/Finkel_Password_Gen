import random

## Password Generator

uppercase_letters = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z']
lowercase_letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z']
password_symbols = [
    '!', '@', '#', '$', '%', '^', '&', '*',
    '(', ')', '-', '_', '=', '+', '[', ']',
    '{', '}', ';', ':', "'", '"', ',', '.',
    '<', '>', '/', '?', '\\', '|', '`', '~']

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,]

print("Welcome to the password generator")
num_letters = int(input("How many letters would you like? "))
num_lilletters = int(input("How many lilletters would you like? "))
num_symbols = int(input("How many symbols would you like? "))
num_numbers = int(input("How many numbers would you like? "))

password = ""

for letter in range(1, num_letters + 1):
    password += random.choice(uppercase_letters)
for lower_case in range(1, num_lilletters + 1):
    password += random.choice(lowercase_letters)
for symbol in range(1, num_symbols + 1):
    password += random.choice(password_symbols)
for number in range(1, num_numbers + 1):
    password += str(random.choice(numbers))

print(f"Your password is: {password}")
print("Thank you for using Finkel Funny Generator")