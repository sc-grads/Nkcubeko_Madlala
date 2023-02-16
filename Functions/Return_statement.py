
n = len([1, 2, 3, 5])
print(n)

def add1(a, b):
    print(f'Sum: {a + b}')

def add2(a, b):
    return a + b

def fun1():
    pass


add1(3, 4)
my_sum = add2(2, 8)
print(my_sum)

x = fun1()
print(x)
print(add1(4,5))

def my_func(x):
    return x, x **2, x**3, x**4

print(my_func(3))
a, b, c, d = my_func(5)
print(a, b, c, d)
x, *y = my_func(4)
print(x, y)




