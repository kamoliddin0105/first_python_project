import math,random

fruits = ["Apple", "Banana", "Orange", "Grapes", "Mango", "Pineapple", "Strawberry", "Cherry"]
print(fruits)

fruits_len = list(filter(lambda fruit: len(fruit) >= 6, fruits))
print(fruits_len)

letter = 'C'

fruits_c = list(filter(lambda fruit: fruit.startswith(letter), fruits))
print(fruits_c)

nums = random.sample(range(1, 100), 10)
print(nums)

even_number = list(filter(lambda num: num % 2 == 0, nums))
print(even_number)


space = lambda pi,r : 2*pi*r
print(space(math.pi,10))

degree = lambda x,y : x ** y
print(degree(5,3))

def degree(n):
    return lambda x : x**n

kvadrat = degree(2)
print(kvadrat(10))

kub = degree(3)
print(kub(9))

nums = range(1,11)
roots = list(map(math.sqrt, nums))
print(roots)


