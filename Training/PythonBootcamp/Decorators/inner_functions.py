
def outer():
    mssg = 'Python'
    y = 2
    def inner():
        print(f'{mssg} is really cool!') # is a free variable(non-local)
        nonlocal y
        y += 1
        print(y)

    inner()
outer()


# defining an outer function
def outers():
    msg = 'Python'
    x = 0

    # defining an inner function
    def inners():
        # nonlocal is used to declare that a variable inside a nested function
        # is not local to it (it lies in the outer enclosing function).
        nonlocal x  # this is `x` from outer function
        x += 1
        print(f'{msg} is really cool!')  # `msg` and `x` are free variables
        return x

    return inners


func1 = outers()
print(type(func1))  # => <class 'function'>

xx = func1()
print(xx)  # => 1

print(func1())  # => 2
print(func1())  # => 3






