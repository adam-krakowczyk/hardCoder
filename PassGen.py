# # PASSWORD #GENERATOR
# Napisz program do generowania losowych haseł o zadanej przez użytkownika długości.
# Hasło musi spełniać zadane warunki np. co najmniej jedna liczba,
# co najmniej po jednej dużej i małej literze.
# Warto skorzystać z modułów string i secrets.
# Propozycja rozszerzenia:
# Po wygenerowaniu hasła skopiuj je do schowka systemowego


import random
import string
import secrets
from pyperclip import copy


def param_pass(lenght, digit=1, upper=1, special=1):
    password = ''
    if digit > 0:
        pattern = string.digits
        for i in range(digit):
            password += secrets.choice(pattern)
    if upper > 0:
        pattern = string.ascii_uppercase
        for i in range(upper):
            password += secrets.choice(pattern)
    if special > 0:
        pattern = string.punctuation
        for i in range(special):
            password += secrets.choice(pattern)
    if len(password) < lenght:
        pattern = string.ascii_lowercase
        for i in range(int(lenght)-int(len(password))):
            password += secrets.choice(pattern)
    passwordList = list(password)
    random.SystemRandom().shuffle(passwordList)
    password = ''.join(passwordList)
    return password


password = param_pass(int(input("Pleas tape password lenght: ")))
print(f'You generated password (use Ctr + v): {password}')
copy(password)
