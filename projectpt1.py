import re
import math

def password_strength(password):
    length = len(password)
    score = 0
    feedback = []

    if length >= 12:
        score += 2
    elif length >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    if re.search(r"[a-z]", password): score += 1
    else: feedback.append("Add lowercase letters.")
    if re.search(r"[A-Z]", password): score += 1
    else: feedback.append("Add uppercase letters.")
    if re.search(r"[^a-zA-Z0-9]", password): score += 1
    else: feedback.append("Add special characters.")

    if score<= 2:
        strength = "Weak"
    elif score == 3: 
        strength = "Medium"
    elif score == 4:
        strength = "Strong"
    elif score == 5:
        "Very Strong"

    return strength, feedback

user_password = input("Enter a password to test: ")
print(password_strength(user_password))