# Importing the re module lets ususe regular expressions
import re

# This is importing the 'math' module, although it isn't used in the script
import math

# Defines a function that checks the strength of a password

def password_strength(password):
    
    # Measures the length of password
    length = len(password)
    
    # Score counter starts at 0
    score = 0
    
    # A list to hold feedback messages for the user
    feedback = []
    
    # Checks the length of the password
    if length >= 12:
        
        score += 2 # It gives two points if it's 12 or more characters
    elif length >= 8:
        
        score += 1 # It gives one point if it's at least 8 character
    else:
        
        feedback.append("Use at least 8 characters.") # This will recommend improvement if password is too short

    # Seeing if password has lowercase letters and says to add lowercase letters if there is none
    if re.search(r"[a-z]", password): 
        score += 1
    else: feedback.append("Add lowercase letters.")

    # Seeing if the password has uppercase letters and says to add uppercase if there is none
    if re.search(r"[A-Z]", password): 
        score += 1
    else: feedback.append("Add uppercase letters.")
        
    if re.search(r"[^a-zA-Z0-9]", password): 
        score += 1
    else: feedback.append("Add special characters.")

    # Labeling the strength based on score
    if score<= 2:
        strength = "Weak"
    elif score == 3: 
        strength = "Medium"
    elif score == 4:
        strength = "Strong"
    elif score == 5: # This line isn't used for this code
        "Very Strong"
    # This returns the feedback for if any of the uppercase, lowercase, special characters were not used
    return strength, feedback
    
# Will ask the user to enter a password
user_password = input("Enter a password to test: ")

# Prints out user's password and print the result
print(password_strength(user_password))
