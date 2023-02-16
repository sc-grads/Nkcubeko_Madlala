
def differenc(a, b):
    result = a - b
    print(result)
differenc(10, 4)

def fun1(x, y, z):
    print(f'1st parameter is x {x}')
    print(f'2nd parameter is y {y}')
    print(f'3rd parameter is z {z}')

fun1(y=4, x=3, z=7)
fun1(10, z=20, y=30)
# fun1(x=2, 3, z=5) this is WRONG, ERROR!!!

def add(x, y=10, z=7):
    print(f'x is {x}, y is {y} and z is {z}')
    print(f'{x} + {y} + {z} = {x + y + z}')

add(2)
add(3, 4, 8)

add(x=3, z= 6)






















