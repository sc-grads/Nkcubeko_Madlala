x = 5 # creating a variable x that stores an integer(5)
print(x)
a, b, c = 3, 7, 8
print(a)
print(b)
print(c)
name, age = "Nkcubeko", 30
print(name)
print(age)
print(type(name))
print(id(name))

print(age == 30)
print(age < 20)
print(age >= 27)
print(len(name))
print(len(name) != 8)

person = ["Dave", 34, "African", [2, 4, 8]]
print(person)

# Maths operators
print(3 + 2)
print(4 - 1)
print(5 * 2)
print(12 / 3)
print(3 ** 2)
print(7 // 2)
print(20 % 3)
print(3 + 2 * 4 ** 2)

print(2000 == 2_000)

k = 4
k += 2
print(k)
k -= 3
print(k)
k *= 2
print(k)
k /= 2
print(k)
k **= 3

c, d = divmod(15, 7)
print(c, d)
print(pow(5, 2))
print(sum([2, 4, 3, 1, 5]))
print(min([12, 2, 4, 13, 8, 7, 10]))
print(max([12, 2, 4, 13, 8, 7, 10]))

n = 3.26754138
print(round(n, 3))
numbers = [1, 2, 3, 4]
print(id(numbers))
numbers.append(20)
print(numbers)

nums = numbers.copy()
print(nums == numbers)
print(nums is numbers)
#Floating point Arithmetic
print(0.125 == 1/10 + 2/100 + 5/1000)
print(format(1/3, '.20f'))

f = 0.1 * 3
g = 0.3
print(f == g)
print(format(f, '.25'))
print(format(g, '.25'))

from math import isclose
x = 0.000001
y = 0.000002
print(x == y)
print(isclose(x, y, abs_tol=0.01))
a = 999999.01
b = 999999.02
print(isclose(a, b, rel_tol=0.01))

a = 3.4
b = 2.3
print(a + b)
print(format(a, '.25f'))
print(format(b, '.25f'))





