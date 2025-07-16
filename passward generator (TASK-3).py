import random
import string

def generate_pass(length,strength):
    if strength == "weak":
        chars = string.ascii_lowercase
    elif strength == "medium":
        chars = string.ascii_letters + string.digits
    elif strength == "strong":
        chars = string.ascii_letters + string.digits + string.punctuation
    else:
        print("Invalid strength option.")
        return None

    password = ''.join(random.choice(chars)for _ in range(length))
    return password

print("PASSWORD GENERATOR")

while True: 
    try:
        length = int(input("Enter the password length: "))
        if length>0:
            break
        else:
            print("Length must must be a positive number.")
    except ValueError:
        print("Please enter a valid number.")

while True:
    strength = input("enter strength(weak/ medium/ strong): ").lower()
    if strength in["weak", "medium", "strong"]:
        break
    else:
        print("Please Choose")

password = generate_pass(length,strength)
print(f"Generated {strength.capitalize()} Password: {password}")