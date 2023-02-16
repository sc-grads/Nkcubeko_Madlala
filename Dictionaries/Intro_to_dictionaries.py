
person = {'name': 'John', 'age': 30, (1, 2, 3): 100}
print(type(person))
d1 = dict()
print(person)
print(len(person))

person['name'] = 'Dan'
print(person)
person['location'] = 'Berlin'
print(person)

a = person['age']
print(a)
value = person.get('city', 'key does not exist')
print(value)
name = person.pop('name')
print(name, person)

print(person.popitem())

del person['age']
print(person)

germany = {
    'cities': ['Hamburg', 'Berlin', 'Munich'],
    'info': {'population': 83_000_000, 'people': ['Einstein', 'Bach', 'Gauss']}
}
print(germany)
print(germany['cities'][1])
print(germany['info']['people'][0])

countries = [
    {'cities': ['Hamburg', 'Berlin', 'Munich'],
    'info': {'population': 83_000_000, 'people': ['Einstein', 'Bach', 'Gauss']}
     },
    {'cities': ['Paris', 'Lyon', 'Bordeaux'],
     'info': {'population': 67_000_000, 'people': ['Monet', 'Marie Curie', 'Napoleon']}
     }
]
print(countries[0]['cities'])
print(countries[1]['info']['people'][1])

































