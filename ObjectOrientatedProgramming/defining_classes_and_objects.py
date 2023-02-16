
class Robot:
    """This class implements a robot"""
    population = 0
    def __init__(self, name, year):
        self.name = name
        self.year = year

        Robot.population += 1
    def __del__(self):
        print('Robot destroyed!')

r1 = Robot('R1', 2023)
print(r1.__doc__)
print(f'Robot name: {r1.name}')

print(r1.__dict__)

print(f'Robots alive: {Robot.population}')







