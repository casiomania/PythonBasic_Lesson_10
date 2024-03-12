# # Lesson 10 / Homework
# Write validations using regular expressions and test them on different cases:
# - Home phone number (only digits and number length)
# - Mobile phone number (only digits, possible plus sign, number length)
# - email (presence of @, domain: gmail.com, for example, minimum length and maximum length of your choice)
# - Full name of the client (3 words, minimum length 2 characters, maximum length 20)
# - Password (minimum: one uppercase letter, one lowercase letter, one digit, one symbol, password length - from 8 to 16 characters)

import re


def home_number_validation(home_number):
    return bool(re.match(r'^\d{5}$', home_number))


def mobile_phone_validation(mobile_number):
    return bool(re.match(r'^\d{10}$', mobile_number))


def email_validation(email):
    return bool(re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email))


def full_name_validation(name):
    return bool(re.match(r'^[a-zA-Zа-яА-Я]{2,20}\s[a-zA-Zа-яА-Я]{2,20}\s[a-zA-Zа-яА-Я]{2,20}$', name))


def password_validation(password):
    return bool(re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,16}$', password))


# testing

print("Home number test:")
print("41592 - correct number")
print(home_number_validation("41592"))
print("415923 - more than 5")
print(home_number_validation("415923"))
print("4159 - less than 5")
print(home_number_validation("41592"))
print("41592abc - contains the letters")
print(home_number_validation("41592abc"))

print("\nMobile number test:")
print("0931234567 - correct number")
print(mobile_phone_validation("0931234567"))
print("093123456 - less than 10 ")
print(mobile_phone_validation("093123456"))
print("09312345678 - more than 10")
print(mobile_phone_validation("09312345678"))
print("0931234567abc - contains the letters")
print(mobile_phone_validation("0931234567abc"))

print("\nTest email:")
print("casiomania@mail.com - correct email")
print(email_validation("casiomania@mail.com"))
print("casiomania@mail - without domain")
print(email_validation("casiomania@mail"))
print("@mail.com - without name")
print(email_validation("@mail.com"))
print("casiomaniamail.com - without @")
print(email_validation("casiomaniamail.com"))

print("\nFull name test::")
print("Taras Hryhorovych Shevchenko - correct form")
print(full_name_validation("Taras Hryhorovych Shevchenko"))
print("Taras Hryhorovych - only two words")
print(full_name_validation("Taras Hryhorovych"))
print("T G S - too short")
print(full_name_validation("T G S"))
print("Taras Hryhorovych Taras Hryhorovych - more than 20")
print(full_name_validation("Taras Hryhorovych Taras Hryhorovych"))

print("\nPassword test:")
print("Casiomania1! - correct password")
print(password_validation("Casiomania1!"))
print("casiomania - missing uppercase letter")
print(password_validation("casiomania"))
print("Casiomania1!Casiomania1! - too long")
print(password_validation("Casiomania1!Casiomania1!"))
print("Casiomani - too short")
print(password_validation("Casiomani"))
