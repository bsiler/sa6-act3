def lambdaMax(maxFunction, numbers):
    maximum = numbers[0]
    for num in numbers:
        maximum = maxFunction(maximum, num)
    return maximum

nums = [1, 2, 6, 1, 20, 9, 21, 10]
print(lambdaMax(lambda x, y: max(x,y), nums))
