#coding:utf-8
import math
from collections import Counter
password = input("Enter a password to analyze:\t")


has_uppercase = any(c.isupper() for c in password)
has_lowercase = any(c.islower() for c in password)
has_digit = any(c.isdigit() for c in password)
has_symbols = any(not c.isalnum() for c in password)

if has_uppercase and has_lowercase and has_digit and has_symbols and len(password) >= 14:
    print(f'The length is: {len(password)} and has uppercase, lowercase, digit, and symbol characters. It is perfectly strong')
    if has_uppercase and has_lowercase and has_digit and has_symbols and len(password) >= 6 and len(password) < 14:
        print(f'The length is: {len(password)} and has uppercase, lowercase, digit, and symbol characters. It is strong but can be cracked')
    if has_uppercase and has_lowercase and has_digit and has_symbols and len(password) < 6:
        print(f'The length is: {len(password)} surely it has uppercase, lowercase, digit, and symbol characters. It is too short and can be easily cracked')
else:
    print(f'The length is: {len(password)} and it does not have all character types. It is weak and can be easily cracked')

"""
  Using the shannon entropy formula, we can calculate the entropy of a password based on its length and character set. The formula is: E = L * log2(N), where E is the entropy, L is the length of the password, and N is the number of possible characters in the character set. The character set can include uppercase letters, lowercase letters, digits, and symbols. The more diverse the character set and the longer the password, the higher the entropy and the stronger the password.
"""

def shannon_entropy(password):
    length = len(password)
    char_set_size = 0
    if has_uppercase:
        char_set_size += 26
    if has_lowercase:
        char_set_size += 26
    if has_digit:
        char_set_size += 10
    if has_symbols:
        char_set_size += 32 #"Assumming that the most common symbols are 32 in total

        entropy = len(password) * math.log2(char_set_size)
        return entropy
