
my_tuple = (1.4, 10, 'abc', True, (20, 30), 'x')
t1 = my_tuple + tuple('yz')
print(t1)

t2 = (1, 2, 'a') * 3
print(t2)

print(my_tuple[:2])
print(my_tuple[::])
print(my_tuple[-1][-1])

movies = ('The Uninvited Guest', 'The Equalizer', 'Colombiana')
for movie in movies:
    print(f'We are watching: {movie}')

print('Colombiana' in movies)
print('Colombiana' not in movies)









