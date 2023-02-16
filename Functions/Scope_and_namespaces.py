
t1 = tuple(range(20))
print(t1)

numbers = [1, 2, 3]
x = 10
def my_function(numbers, x):
    numbers.append(5)
    x = 66
    print(f'x inside the funcion: {x}')

my_function(numbers, x)
print(f'After calling the function, numbers is {numbers} and x is {x} ')






