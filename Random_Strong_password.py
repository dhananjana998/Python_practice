#random strong password generator

import random
import string


length= int(input("Enter length password length:"))

letters=string.ascii_letters
digits=string.digits
symbols=string.punctuation

all_characters= letters+digits+symbols

password=''.join(random.choice(all_characters) for i in range(length))

print("Your strong password is:", password)

""" output:

Enter length password length:8

Your strong password is: U^3qaG|S

"""