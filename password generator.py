# libarys 
import random
import string

# define function
def generate_password(length, uppercase=True, lowercase=True, digits=True, symbols=True):
    characters = ''
    #if upercase do this
    if uppercase:
        characters += string.ascii_uppercase
    #if lowercase do this
    if lowercase:
        characters += string.ascii_lowercase
    #if digits do this
    if digits:
        characters += string.digits
    #if symbols do this 
    if symbols:
        characters += string.punctuation

    if not any((uppercase, lowercase, digits, symbols)):
        print("Please enable at least one character type.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    
    #whats returned
    return password

def main():
    print("Welcome to Password Generator!")

    while True:
        try:
            length = int(input("Enter the length of the password: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    digits = input("Include digits? (y/n): ").lower() == 'y'
    symbols = input("Include symbols? (y/n): ").lower() == 'y'

    password = generate_password(length, uppercase, lowercase, digits, symbols)
    if password:
        print("Your generated password is:", password)




