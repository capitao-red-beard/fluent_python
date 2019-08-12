import os


# Using tuples as records.

# Lat and Long of LAX airport.
lax_coordinates = (33.9425, -118.408056)

# Data about Tokyo: name, year, population, (millions), 
# population change (%), area (km2).
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)

# A list of tuples of the form (country_code, passport_number).
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]

# As we iterate over the list, passport is bound to each tuple.
for passport in sorted(traveler_ids):
    # The % operator understands tuples and treats each item as a 
    # separate field.
    print('%s/%s' % passport)

# The for loop knows how to retrieve the items of a tuple separately -
# this is called "unpacking". Here we are not interested in the second 
# item, so it is assigned to _, a dummy variable.
for country, _ in traveler_ids:
    print(country)

# Tuple Unpacking.

# Parallel assignment, assigning items from an itereable to a tuple of 
# variables.
latitude, longitude = lax_coordinates # Tuple unpacking.
print(latitude)
print(longitude)

# We can also swap variable order using unpacking.
latitude, longitude = longitude, latitude

# Prefixing an argument with a star when calling a function.
v = divmod(20, 8)
print(v)
t = (20, 8)
v2 = divmod(*t)
print(v2)
quotient, remainder = divmod(*t)
print(quotient, remainder)

# We can also use tuple unpacking to return mutliple values in a way 
# which is conventient to the caller. os.path.split() builds a tuple
# (path, last_part) from a filesystem path.
_, filename = os.path.split(
    r'C:\Users\av10\VisualStudioProjects\fluent_python\tewples.py')
print(filename)

# Using * to grab excess items, defining function parameters with *args 
# to grab arbitrary excess arguments in calssicly Pythonic
a, b, *rest = range(5)
print(a, b, *rest)
a, b, *rest = range(3)
print(a, b, *rest)
a, b, *rest = range(2)
print(a, b, *rest)

# The * prefix can be used in any position
a, *body, c, d = range(5)
print(a, *body, c, d)
*head, b, c, d = range(5)
print(*head, b, c, d)

# It also works to unpack nested tuples
# Each tuple holds a record with four fields, the last of which is a 
# cooridnate pair.
metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paolo', 'BR', 19.649, (-23.547778, -46.635833)),
]
print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
# By assigning the last field to a tuple, we unpack the coordinates.
for name, cc, pop, (latitude, longitude) in metro_areas:
    # Limit the output to metropolitan areas in the western hemisphere.
    if longitude <= 0:
        print(fmt.format(name, latitude, longitude))
