
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

# The value of the constant PI with many decimal points
PI = 3.141592653589793

# Convert it to 4 decimal points, format() returns a string
PI = format(PI, '.5f')
PI = float(PI)  # convert PI which is a string to a float

print(PI)  # => 3.14159