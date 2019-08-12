import array

# Initializing a tuple from a generator expression.
symbols = '$&@*^%'
t = tuple(ord(symbol) for symbol in symbols)
print(t)

# Initializing an array from a generator expression
a = array.array('I', (ord(symbol) for symbol in symbols))
print(a)

# Generator expressions yield items one by one, saving memory 
# when compared to list comprehension which creates a list in memory.
colours = ['black', 'white']
sizes = ['S', 'M', 'L']
for tshirt in ('%s %s' % (c, s) for c in colours for s in sizes):
    print(tshirt)
