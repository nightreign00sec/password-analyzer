def load_common_passwords(filepath="data/common_passwords.txt"): #Load the file and check if the password is in the file
    with open(filepath, 'r') as f:
        passwords = f.read().splitlines()
    return set(passwords)

def is_common_password(password, common_passwords):
    return password in common_passwords
