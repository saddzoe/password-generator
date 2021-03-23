# password-generator
# This program will help generate a password for the user.

import random

password_length = int(input("enter the length of password: "))
password_char: str = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
password = "".join(random.sample(password_char, password_length ))

print(password)
