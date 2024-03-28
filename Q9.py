
from functools import reduce

list = [1, 2, 3, 4, 5]
def multiply(x, y):
    return x * y
product = reduce(multiply, list)
print("The product of the numbers is:", product)