#!/usr/bin/env python3

import random
import string

# Define the possible chars to use in the password
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation

    # Use random.choices to pick 'length' number of characters from the pool og 'characters'
    password = ''.join(random.choices(characters, k=length))

    return password


# example usage: Generate a random password with length of '8'
password = generate_password(8)

print(password)
