import random

upperCharacter = [chr(i + 65) for i in range(26)]
lowerCharacter = [chr(i + 97) for i in range(26)]
numbers = [chr(i + 48) for i in range(10)]
symbols = [33, 35, 36, 37, 38, 64]
symbols = [chr(x) for x in symbols]

def generatePassword():
    password = []

    password.append(random.choice(upperCharacter))
    for i in range(7):
        password.append(random.choice(lowerCharacter))
    password.append(random.choice(symbols))
    for i in range(2):
        password.append(random.choice(numbers))

    return "".join(password)

password = generatePassword()
print(f"Password : {password}")
