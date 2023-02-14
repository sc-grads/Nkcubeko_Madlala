#
print(x := 2 + 3)
print(f'x is {x}')

value = input('Enter something: ')
while value != '':
    print(f'you have entered: {value}')
    value = input('Enter something: ')

while(value := input('Enter something: ')) != '':
    print(f'you have entered: {value}')

data = input('Enter your name: ')
if len(data) > 0:
    print(f'Your name has {len(data)} characters.')
else:
    print('Your name cannot be empty!')