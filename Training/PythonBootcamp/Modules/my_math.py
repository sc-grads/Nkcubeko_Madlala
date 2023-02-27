
x = 5
def my_sum(*args):
    y = 0
    for value in args:
        y = y + value
    return y

print('Message printed inside my_math.py')
y = my_sum(1, 5, 7)
print(f'sum calculated inside my_math.py is {y}')