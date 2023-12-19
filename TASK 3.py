import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")

    try:
        length = int(input("Enter the desired length of the password: "))
    except ValueError:
        print("Invalid input. Please enter a valid numeric value for the password length.")
        return

    if length <= 0:
        print("Invalid password length. Please enter a positive integer.")
        return

    password = generate_password(length)

    print(f"\nGenerated Password: {password}")

if __name__ == "__main__":
    main()
