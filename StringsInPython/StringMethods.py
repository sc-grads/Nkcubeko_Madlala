#String Methods
#print(), len(), min(), max(), type(), sum(), round()
print(len('xfdsa'))
print(dir(str))
help(str.replace)

s = 'Python'
print(s)
new_s = s.upper()
print(new_s)
print('pRoGrAmiNg'.lower())

ip = '  192.168.0.1    '
ip = ip.strip()
print(ip)

value = '$$$300$$$$$'
print(value.strip('$'))

new_value = value.replace('$', '*')
print(new_value)
txt = ' I learn Python, Python is cool!'
n = txt.count('Python')
print(n)
txt = ' I learn PythoN, PyThon is cool!'
n = txt.lower().count('python')
print(n)
print(txt.count('y'))
print(txt.count('i'))

my_txt = txt.split()
print(my_txt)
p = '12.2.1.3.4.23.15.9'
my_p = p.split('.')
print(my_p)

new_p = ','.join(my_p)
print(new_p)

txt = 'I learn Python, it is cool!'

print(txt.find('learn'))

print('it' in txt)

print('cool' not in txt)
print('good' in txt)





