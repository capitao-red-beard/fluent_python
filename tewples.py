import os
from collections import namedtuple, OrderedDict


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

# Named Tuples.

# Defining a named tuple used to hold information about a city.
# Two parameters are required to create a named tuple: a class name and 
# a list of field names, which can be given as an iterable of strings
# or as a single space delimeted string (as in the example below).
City = namedtuple('City', 'name country population coordinates')
# Data must be passed as positional arguments to the constructor 
# (in contrast the tuple takes a single iterable).
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
print(tokyo)
# Fields can be accessed ny name or position.
print(tokyo.population)
print(tokyo.coordinates)
print([tokyo[1]])

# Named tuple has a few attributes alongside the inhereted ones from
# tuple. The most useful are: _fields - (class attribute),
# _make(iterable) - (class method) and _asdict() - (instance method).
# _fields is a tuple with the field names of the class.
print(City._fields)
LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
# _make() allow you to instatiate a named tuple from an iterable.
delhi = City._make(delhi_data)
# _asdict() returns a collections.OrderedDict built from the named 
# tuple instance. Used to produce a nice display of city data.
print(delhi._asdict())
OrderedDict([('name', 'Delhi NCR'), ('country', 'IN'), ('population', 21.935),
             ('coordinates', LatLong(lat=28.613889, long=77.208889))])
for key, value in delhi._asdict().items():
    print(f'{key} : {value}')

# Slicing: [start:stop:step].
l = [10, 20, 30, 40, 50, 60]
# Splits at 2.
print(l[:2])
# Splits at 3.
print(l[:3])
print(l[3:])
# Slicing Objects.
s = 'bicycle'
# Every third value.
print(s[::3])
# Reversed.
print(s[::-1])
# Reversed every other value.
print(s[::-2])
