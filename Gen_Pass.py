import random
import string

def generate_password(length):
    uppercase = string.ascii_uppercase      # ABCDEFGHIJKLMNOPQRSTUVWXYZ
    lowercase = string.ascii_lowercase      # abcdefghijklmnopqrstuvwxyz
    numbers = string.digits                 # 0123456789
    symbols = string.punctuation            # !@#$%^&*()_+ 

    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(numbers),
        random.choice(symbols)
    ]


    all_characters = uppercase + lowercase + numbers + symbols

    for _ in range(length - 4):
        password.append(random.choice(all_characters))

    random.shuffle(password)

    return ''.join(password)

length = int(input("Enter password length: "))

if length < 4:
    print("Password length should be at least 4")
else:
    print("Generated Password:", generate_password(length))


