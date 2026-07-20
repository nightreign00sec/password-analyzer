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
  Using the shannon entropy formula, we can calculate the entropy of a password based on its length and character set. which is H = -sum(p(x) * log2(p(x))) for each unique character x in the password, where p(x) is the probability of character x occurring in the password. The more diverse the character set and the longer the password, the higher the entropy and the stronger the password.
"""

def shannon_entropy(password: str) -> float:
    length = len(password)
    if length == 0:
        entropy = 0.0
    #count the freq of each character
    counts = Counter(password)

    #shannon entropy formula H = -sum(p(x) * log2(p(x))) for each unique character x in the password, where p(x) is the probability of character x occurring in the password.
    entropy = -sum((count / length) * math.log2(count / length) for count in counts.values())
    return entropy


print(f'The shannon entropy of the password is : {shannon_entropy(password)} bits')

