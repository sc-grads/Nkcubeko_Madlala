#Formatting the Strings

first_name = 'John'
last_name = 'Smith'
age = 36
print('Hello! ' + first_name + ' ' + last_name + '! You are ' + str(age) + ' years old.')
print(f'Hello! {first_name} {last_name}! You are {age} years old.')

s = f'{2.3 * 4.1 / 5.2}'
print(s)
s = f'{2.3 * 4.1 / 5.2:.4f}'
print(s)
#fahrenheit = celsius * 1.8 + 32
celsius = 15.4
print(f'{celsius} Degrees Celsius = {celsius * 1.8 + 32} Degrees Fahrenheit.')











