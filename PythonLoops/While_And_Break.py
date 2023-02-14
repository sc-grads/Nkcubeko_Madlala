
# while True:
#     guess = int(input('Enter your lucky number [1-10]:'))
#     if guess == 7:
#         print('You Won!!!')
#         break
#     print(f'Sorry, {guess} was not a lucky number!')

a = int(input('Enter a number:'))
while a > 1:
    b = a // 2
    while b > 1:
        if a % b == 0:
            break
        b -= 1
    else:
        print(f'{a} is a prime number')
    a -= 1


