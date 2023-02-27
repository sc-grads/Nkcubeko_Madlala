# f = open('configuration.txt', 'rt')
# content = f.read()
# print(content)
# f.close()
# print(f.closed) # will return "True"

# with open('ip.txt') as f:
#      ip_list = f.read().splitlines()
#      f.write('Some text here.\n')


print('#' * 30, ' DONE!!!', '#' * 30)

with open('show_arp.txt', 'r', newline='') as f:
    # Reading file in list (each line is list element)
    contents = f.read().splitlines()

    # The argument newline='' is necessary only in Windows

    # Eliminating the first item from the list (files header)
    contents = contents[1:]

    # Empty list that stores tuples like (ip, mac)
    ip_mac = list()

    # Iterating over the list(file contents) line by line
    for line in contents:
        ip = line.split()[1]  ## Getting the IP
        mac = line.split()[3]  ## Getting the MAC

        # Adding the tuple to the ip_mac list
        ip_mac.append((ip, mac))

    print(
        ip_mac)  # [('192.168.122.10', 'aabb.cc00.0200'), ('192.168.122.20', 'aabb.cc00.0100'), ('192.168.122.30', 'aabb.cc00.0300')]

## show_arp.txt contents:
# Protocol  Address          Age (min)  Hardware Addr   Type   Interface
# Internet  192.168.122.10          -   aabb.cc00.0200  ARPA   Ethernet0/0
# Internet  192.168.122.20          0   aabb.cc00.0100  ARPA   Ethernet0/0
# Internet  192.168.122.30          0   aabb.cc00.0300  ARPA   Ethernet0/0


# Opening the file in read only mode
f = open('a.txt', 'r')

# Move the cursor on position 4 inside the file
f.seek(4)

# Read 5 characters starting with position 4 and return them in variable called word
word = f.read(5)
print(word)  # => first

# Closing the file
f.close()

# Opening the file in append mode
with open('workout.txt', 'a') as file:
    file.write('May 25:8800\n')  # appending to the end of the file





