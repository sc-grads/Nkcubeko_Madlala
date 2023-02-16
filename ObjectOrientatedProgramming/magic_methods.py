
class Robot:
    """This class implements a robot"""
    population = 0
    def __init__(self, name, price):
        self.name = name
        self.price = price

        Robot.population += 1
    def __del__(self):
        print('Robot destroyed!')
    def __str__(self):
        my_str = f'My name is {self.name} and my price is {self.price}'
        return my_str
    def __add__(self, other):
        price = self.price + other.price
        return price


r1 = Robot('Marvin', 150)
r2 = Robot('Gal', 45)

print(r1)
print(r2)

print(r1 + r2)










