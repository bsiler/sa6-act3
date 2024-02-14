strings = ['abe', 'foot', 'be', 'a', 'cat', 'twenty']
sortedStrings = sorted(strings, key = lambda x: (len(x), x[0]))
print(sortedStrings)