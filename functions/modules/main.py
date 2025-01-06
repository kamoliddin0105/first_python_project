from car_info_mod import car_info as cinfo, info_print as iprint
import math,random

y = list(range(0,10))
print(y)
random.shuffle(y)
print(y)

x = list(range(0,101,5))
print(random.choice(x))

names = ['husan','hasan','begzod']
name = random.choice(names)
print(random.choice(name))

print(random.randint(0,100))

print(math.pow(5,3))

car = cinfo("Chevrolet","Lacetti","White","mexanika",2012,12000)
iprint(car)
