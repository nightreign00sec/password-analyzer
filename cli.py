#coding:utf-8
from analyzer.entropy import calculate_entropy
from analyzer.entropy import char_set_detector
from analyzer.wordlist import load_common_passwords, is_common_password
password = input("Enter a password to analyze:\t")


char_set_detector(password)
calculate_entropy(password)
is_common_password(password, load_common_passwords())

common_passwords = load_common_passwords()
if is_common_password(password, common_passwords):
    print("The password is a common password. Please choose a stronger one.")
else:
    print("Nice this is not a common password.")
