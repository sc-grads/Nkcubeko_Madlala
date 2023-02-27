mystr = "Hello Python!"
print(mystr)
print('I\'m fine')
message = 'He said: "Go for it!"'
print(message)
languages = """I like Python
SQL, R and
C++
"""
print(languages)
my_languages = 'I like Python\nSQL\nR\nand\nC++'
print(my_languages)
print('a\tb\tc\td\ne')
print('\\n')

name = input('Enter your name:')
print('Your name is', name)

price = input('Enter price:')
quantity = input('Enter quantity:')
total_value = float(price) * float(quantity)
print(total_value)

miles = input('Enter distance in miles:')
miles = float(miles)

a = 10
b = 2.3
c = "5.4"
#convert int to float

a_float = float(a)
print('a:', type(a))
print('a_float:', type(a_float))

# float =>
b_str = str(b)
print('b:', type(b))
print('b_str:', type(b_str))

# str => int

print('c:', type(c))
c_int = int(float(c))
print('c_int:', type(c_int))

music = 'Deep House'
print(music[0])
print(music[2])
print(music[5])
print(music[-3])
print(music[-1])
print(len(music))
n = len(music)
print(music[n-1])
#concatinating
singer = 'Dj Ace'
music_and_singer = music +    singer
print(music_and_singer)
print(music +     ' Was sung by '   +    singer)

print('abc' '123')

language = 'Python'
version = 3.11
print(language  +  str(version))

# Repetition operator
print(music * 5)
print('#' * 60)
price = 8.5
print(float(price) * 5)














