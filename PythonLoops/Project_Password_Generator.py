import random
import string

chars = string.ascii_letters + string.digits + string.punctuation
print(random.choice(chars))
#length = 12
length = int(input('Passwoed length: '))
password = ' '

for _ in range(length):
    c = random.choice(chars)
    password += c
    print(f'Your random password is: {password}')