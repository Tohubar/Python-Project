import random
import string

def generate_password(min_length, numbers = True, special_character = True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    characters = letters
    
    if numbers:
        characters += digits
    if special_character:
        characters += special
    
    password = ""
    meet_condition = False
    has_number = False
    has_special = False
    while not meet_condition or  len(password) < min_length:
        new_char = random.choice(characters)
        password +=new_char
        
        if new_char in digits:
            has_number = True
        if new_char in special:
            has_special = True
        
        meet_condition = True
        if numbers:
            meet_condition = has_number
        if special_character:
            meet_condition = meet_condition and has_special
        
    return password; 

length = int(input("Enter the length of your password: "))
has_num = input("Do you want to add numbers in password (y/n)? ") == "y"   
has_char = input("Do you want to add special characters in password (y/n)? ") == "y"  
 
p = generate_password(length, has_num, has_char)
print(p)

 
    
