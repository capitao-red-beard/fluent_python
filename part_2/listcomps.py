# Example for why list comprehension is more readable than for loops.

# Build a list of Unicode codepoints from a string (1)
symbols = '$&@*^%'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))
print(codes)

# Build a list of Unicode codepoints from a string (2)
symbols2 = '$&@*^%'
codes2 = [ord(symbol2) for symbol2 in symbols2]
print(codes2)

# Cartesian products using lists
colours = ['black', 'white']
sizes = ['S', 'M', 'L']

# Resulting list is arranged as if the for loops were nested in the
# same order as they appear in the list comprehension.
tshirts = [(colour, size) for colour in colours for size in sizes]
print(tshirts)