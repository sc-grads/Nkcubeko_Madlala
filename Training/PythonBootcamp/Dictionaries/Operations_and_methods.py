
person = {'name': 'John', 'age': 30, 'location': 'USA'}
friend = person

person['name'] = 'Peter'
print(friend)

neighbour = person.copy()
person['location'] = 'Europe'
print(neighbour, person)

countries = {'ro': 'Romania', 'us': 'United States of America', 'ge': 'Germany'}
countries.update({'hu': 'Hungray', 'fr': 'France'})
print(countries)

person.clear()
print(person, friend)

person = {'name': 'John', 'age': 30, 'location': 'USA'}
k = person.keys()
print(k)
print(type(k))
my_keys = list(k)
print(my_keys)

print(person.values())
print(list(person.values()))

print(person.items())
print('name' in person)
print(10 in person.keys())
print('USA' in person.values())
print(('age', 30) in person.items())

d1 = {10: 'a', 20: 'b', 30: 'c'}
v = d1.values()
d1[10] = 'X'
print(v)

d1 = {10: 'a', 20: 'b'}
d2 = {20: 'c', 30: 'c'}
k1 = d1.keys()
k2 = d2.keys()
print(k1, k2)

print(k1 & k2)
print(k1 | k2)

for k in person:
    print(f'Key is: {k}')

for v in person.values():
    print(f'Value is {v}')

for k,v in person.items():
    print(f'Key is {k} and value is {v}')








































