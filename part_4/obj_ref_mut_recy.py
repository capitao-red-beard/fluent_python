import copy


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
