"""
Project name : Generating Password
Author : Khusanboy Sobirjonov
Create date : 1/09/2023 00:04 AM
Telegram : @uzbek_coder_2022
"""
import random   
import secrets 

def generatingPassword(length = 8) -> str:
    """
    Enter the password length, default is 8. 
    Create a password for yourself.
    """
    if length < 8: 
        return "Make sure the password length is not less than 8!!!"
        
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
    
    lower_characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                         'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                         'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                         'z']
     
    upper_characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                         'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                         'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                         'Z']
     
    punctuation = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', 
                   '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', 
                   '?', '@', '[', '\\', ']', '^', '_', '`','{', '|', 
                   '}', '~']
    
    password = ''.join((secrets.choice(digits + lower_characters + upper_characters + punctuation)) for i in range(length))
    
    return password
    
passlength = input("Enter the password length :\n(type n to skip) >>> ")
print(generatingPassword(int(passlength))) if passlength != 'n' else print(generatingPassword())


    
    
    
    
    
    
    
    
    
    