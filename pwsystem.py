import random
import string

#list of common password
common password=["123456","password","123456789","qwerty","abc123","11111111","password123","admin"]

#function to check password strength
def check_password(password):
    has_upper=False
    has_lower=False
    has_number=False
    has_special=False

    special_characters="!@#$%^&*()-_=+[]{};:',.<>?/\|~`"

    for char in password:
        if char.isupper():
            has_upper=True
        
