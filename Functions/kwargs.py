
def my_function(**kwargs):
    print(kwargs)
    for k,v in kwargs.items():
        print(f'k is {k} and v is {v}')

my_function(name='John', age=40, location='London')
person = {'name': 'Ban', 'age': 25, 'location': 'France'}
my_function(**person)

def connect(ip, port, username, password):
    print(ip, port, username, password)

linux_server = {'ip': '200.0.10.1', 'port': 22, 'username': 'admin1', 'password': 'secretPassword'}
connect(**linux_server)



