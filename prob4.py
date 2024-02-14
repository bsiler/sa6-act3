list1 = ['a', 'b', 'c', '6', '5', '4']
list2 = ['c', 'e', '3', '4', '5']

intersection = list(filter(lambda x: x in list2, list1))
print(intersection)