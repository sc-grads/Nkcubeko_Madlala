
user = {'username': 'js', 'level': 'admin'}
def only_admin(func):
    def wrapper_only_admin(*args, **kwargs):
        if user['level'] == 'admin':
            return  func(*args, **kwargs)
        else:
            raise PermissionError('Permission denied')

    return wrapper_only_admin

@only_admin # @ or pie syntax
def remove_file(f=None):
    import os, os.path
    if os.path.isfile(f):
        os.remove(f)
        print(f'{f} removed!')
    else:
        print('Argument is not a file')


# try:
#     remove_file = only_admin(remove_file)
#     remove_file('a.txt')
# except PermissionError as e:
#     print(e)

try:
    remove_file('a.txt')
except PermissionError as e:
    print(e)

from functools import wraps


# defining a decorator
def timer(fn):
    from time import time

    @wraps(fn)
    def wrapper_timer(*args, **kwargs):  # this is a generic decorator
        start_time = time()  # retrieving the current timestamp
        result = fn(*args, **kwargs)
        end_time = time()
        print(f'{fn.__name__} execution time:{end_time - start_time}')
        return result

    return wrapper_timer


# decorating the function
@timer
def sum_of_powers(n, p):
    nums = [x ** p for x in range(1, n)]
    return sum(nums)


s = sum_of_powers(1000000, 2)
print(s)

s = sum_of_powers(1000000, 3)
print(s)

s = sum_of_powers(1000000, 5)
print(s)

## EXPECTED OUTPUT:

# sum_of_powers execution time:0.33020472526550293
# 333332833333500000
# sum_of_powers execution time:0.33238673210144043
# 249999500000250000000000
# sum_of_powers execution time:0.36234617233276367
# 166666166667083333333333250000000000













