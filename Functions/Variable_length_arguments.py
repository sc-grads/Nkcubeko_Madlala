

def average(a, b, *args):
    print(f'args is {args}')
    return (a + b + sum(args)) / (2 + len(args))

# print(average(4, 5, 6, 7))

def concatenate(*args):
    result = ''
    for tmp in args:
        result += tmp
    return result

r = concatenate('Python', ' 3', '!')
print(r)

res = concatenate('I', 'Love', 'Progamming')
print(res)















