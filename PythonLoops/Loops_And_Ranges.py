#Loops And Ranges

s = 0

for n in range(101):
    s += n
print(f'Sum: {s}')

for _ in range(11):
    print('Do something! ', _)

import random
names = ['Dan', 'James', 'Mary', 'Anah', 'Maria', 'Alex', 'Dave', 'Angela']

for _ in range(5):
    print(f'Choosing Winner. Round {_} ...')
    winner = random.choice(names)
    names.remove(winner)
    print(winner)
    print('*********************')








