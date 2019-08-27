import copy
import weakref


# Variables are not boxes.
a = [1, 2, 3]
b = a
a.append(4)
print(b)


# Variables are assigned to objects only after the object is created.
class Gizmo:
    def __init__(self):
        print(f'Gizmo id: {id(self)}')


# Succeeds.
x = Gizmo()
# Fails.
# y = Gizmo() * 10

# Identity, equality, and aliases.
charles = {'name': 'Charles L. Dodgson', 'born': 1832}
lewis = charles
print(lewis is charles)
print(id(charles), id(lewis))
lewis['balance'] = 950
print(charles)

# Imposter test.
alex = {'name': 'Charles L. Dodgson', 'born': 1832, 'balance': 950}
print(alex == charles)
print(alex is not charles)

# The == operator compares values of an object, is compares identities.

# The relative immutability of tuples.
# t1, even adding values has the same identity but its values have 
# changed.
t1 = (1, 2, [30, 40])
t2 = (1, 2, [30, 40])
print(t1 == t2)
print(id(t1[-1]))
t1[-1].append(99)
print(t1)
print(id(t1[-1]))
print(t1 == t2)

# Copies are shallow by default.
l1 = [3, [55, 44], (7, 8, 9)]
l2 = list(l1)
print(l2 == l1)
print(l2 is l1)
l1.append(100)
l1[1].remove(55)
print('l1:', l1)
print('l2:', l2)
l2[1] += [33, 22]
l2[2] += (10, 11)
print('l1:', l1)
print('l2:', l2)


# Deep and shallow copies of arbitrary objects.
class Bus:

    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)
    
    def pick(self, name):
        self.passengers.append(name)
    
    def drop(self, name):
        self.passengers.remove(name)


bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
bus2 = copy.copy(bus1)
bus3 = copy.deepcopy(bus1)
# Using copy and deepcopy we create 3 distinct Bus instances. 
print(id(bus1), id(bus2), id(bus3))
bus1.drop('Bill')
# After bus1 drops Bill, he is also missing from bus2.
print(bus2.passengers)
# Inspection shows that bus1 and bus2 share the same list object 
# because bus2 is a shallow copy of bus1.
print(id(bus1.passengers), id(bus2.passengers), id(bus3.passengers))
# But bus3 is a deep copy of bus1, so its passengers attribute refers 
# to another list.
print(bus3.passengers)

# Function parameters as references.
def f(a, b):
    a += b
    return a

x = 1
y = 2
print(f(x, y))
# The x number is unchanged.
print(x, y)
a = [1, 2]
b = [3, 4]
print(f(a, b))
# The a list is changed.
print(a, b)
t = (10, 20)
u = (30, 40)
print(f(t, u))
# The t tuple is unchanged.
print(t, u)


class HauntedBus:
    """ A bus model haunted by ghost passangers."""

    # When the passangers argument is not passed, this parameter is 
    # bound to the default list object, which is initially empty.
    def __init__(self, passengers=[]):
        # This assignment makes self.passengers an alias for 
        # passangers, which is itself an alias for the fault list, when 
        # no passangers argument is given.
        self.passengers = passengers
    
    # When the methods .remove() and .append() are used with 
    # self.passangers we are actually mutating the default list, which 
    # is an attribute of the function object.
    def pick(self, name):
        self.passengers.append(name)
    
    def drop(self, name):
        self.passengers.remove(name)


bus1 = HauntedBus(['Alice', 'Bill'])
print(bus1.passengers)
bus1.pick('Charlie')
bus1.drop('Alice')
print(bus1.passengers)
# bus2 starts empty, so the default empty list is applied to 
# self.passangers.
bus2 = HauntedBus()
bus2.pick('Carrie')
print(bus2.passengers)
# bus3 also starts empty, again the default list is assigned.
bus3 = HauntedBus()
print(bus3.passengers)
# The default is no longer empty.
bus3.pick('Dave')
# Now Dave from bus3 appears in bus2.
print(bus2.passengers)
# bus2 and bus3 refer to the same passenger list.
print(bus2.passengers is bus3.passengers)
# bus1 passengers is a distinct list.
print(bus1.passengers)


# Defensive programming with mutable parameters.
class TwilightBus:
    """ A bus that makes passengers vanish."""

    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = passengers
    
    def pick(self, name):
        self.passengers.append(name)
    
    def drop(self, name):
        self.passengers.remove(name)


# In this example we are mutating the original list recieved as an 
# argument.
basketball_team = ['Sue', 'Tina', 'Maya', 'Diana', 'Pat']
bus = TwilightBus(basketball_team)
bus.drop('Tina')
bus.drop('Pat')
print(basketball_team)

# del and garbage collection.
s1 = {1, 2, 3}
# s1 and s2 are aliases referring to the same set.
s2 = s1
def bye():
    print('Gone with the wind...')
# register the bye callback on the object referred by s1.
ender = weakref.finalize(s1, bye)
print(ender.alive)
# del does not delete an object, just the reference to it.
del s1
print(ender.alive)
# Rebinding the last reference, s2 makes {1, 2, 3} unreachable. It is 
# destroyed, the bye callback is invoked, and ender.alive becomes False.
s2 = 'spam'
print(ender.alive)

# Weak references.
a_set = {0, 1}
wref = weakref.ref(a_set)
print(wref)
print(wref())
a_set = {2, 3, 4}
print(wref())
print(wref() is None)
print(wref() is None)


class Cheese:

    def __init__(self, kind):
        self.kind = kind
    
    def __repr__(self):
        return f'Cheese{(self.kind)}'


# stock is a WeakValueDictionary.
stock = weakref.WeakValueDictionary()
catalog = [Cheese('Red Leicester'), Cheese('Tilsit'), 
           Cheese('Brie'), Cheese('Parmesan')]

# The stock maps the name of the cheese to a weak reference to the 
# cheese instance in the catalog.
for cheese in catalog:
    stock[cheese.kind] = cheese

# The stock is complete.
print(sorted(stock.keys()))
del catalog
# After the catalog is deleted, most cheeses are frone from the stock, 
# as expected in WeakValueDictionary.
print(sorted(stock.keys()))
del cheese
print(sorted(stock.keys()))
