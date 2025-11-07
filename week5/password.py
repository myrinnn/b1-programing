def check_min_length(password, min_len=8):
    if len(password) >= min_len:
        return True
    else:
        return False
    
def has_uppercase(password):
    upper = False
    for char in password:
        if char.isupper():
            upper = True
    if upper:
        return True
    else:  
        return False
    
def has_lowercase(password):
    lower = False
    for char in password:
        if char.islower():
            lower = True
    if lower:
        return True
    else:  
        return False
    
def has_digit(password):
    digit = False
    for char in password:
        if char.isdigit():
            digit = True
    if digit:
        return True
    else:  
        return False

def has_special_char(password):
    return any(char in string.punctuation for char in password)
       

import string 
import random 
from collections import namedtuple

def validate_password(password):

    overall = False
    if check_min_length(password) and has_lowercase(password) and has_digit(password) and has_special_char(password):
        overall = True 
        
    bigtuple = namedtuple('Results', ['a', 'b', 'c', 'd', 'e', 'f'])
    results = bigtuple(overall, check_min_length(password), has_uppercase(password), has_lowercase(password), has_digit(password), has_special_char(password))
    
    return results
    
def main():
    print("=" * 50)
    print("PASSWORD STRENGTH VALIDATOR")
    print("=" * 50)
    print()
    print("Password Requirements:")
    print("Minimum 8 characters")
    print("At least one uppercase letter")
    print("At least one lowercase letter")
    print("At least one digit")
    print("At least one special character (!@#$%^&* etc.)") 
    print()
    
    password = input("Enter password to validate: ")
    
    results = validate_password(password)
    
    print()
    print("=" * 50)
    print("VALIDATION RESULTS")
    print("=" * 50)

    
    print("Minimum length (8+ chars): " + str(results.b))
    print("Contains uppercase: " + str(results.c))
    print("Contains lowercase: " + str(results.d))
    print("Contains digit: " + str(results.e))
    print("Contains special character: " + str(results.f))

    print()
    print("=" * 50)

    if results[0]:
        print("PASSWORD ACCEPTABLE")
    else:
        print(" PASSWORD UNACCEPTABLE - Try again")
        
    print("=" * 50)
    
if __name__ == "__main__":
    main()