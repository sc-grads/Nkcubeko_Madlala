# import telnetlib
#
# host = '10.1.1.10'
# port = '23'
# user = 'v1'
# password = 'cisco'
#
# tn = telnetlib.Telnet(host=host, port=port)
# tn.read_until(b'Username: ')
# tn.write(user.encode() + b'\n')
#
# tn.read_until(b'Password: ')
# tn.write(password.encode() + b'\n')
#
# tn.write(b'show ip interface brief\n')
# tn.write(b'exit\n')
#
#
#
