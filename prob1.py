from functools import reduce
number = 303
sumOfDigits = reduce(lambda x, y: int(x) + int(y), str(number))
print(sumOfDigits)