
try:
    a = int(input('Enter a:'))
    b = int(input('Enter b:'))
    c = a / b
    print(c)
except:
    print('An exception has occurred.')
else:
    print('No errors.')
    print(f'c = {c}')
finally:
    print('Good bye...')


x = 3
print(x ** x)
print('Some other code.')








