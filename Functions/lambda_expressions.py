
def add(a, b, c):
    result = a + b + c
    return result

result = (lambda a, b, c: a + b + c)(3, 4, 5)
print(result)

square = lambda x = 3: x** 2
print(square(4))
print(square())

friends = [('Dainaaaaa', 30), ('Aaaaaaaaana', 25), ('Tudor', 22)]
friends.sort(key=lambda x: len(x[0]))
print(friends)







