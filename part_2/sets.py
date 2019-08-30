from dis import dis
from unicodedata import name


# Set theory.
# Set type and its immutable sibling frozenset.
# A set is a collection of unique objects.
l = ["spam", "spam", "eggs", "eggs"]
print(set(l))
print(list(set(l)))

# Set elements must be hashable. The set type itself is not hashable,
# but frozenset is.
"""
found = len(needles & haystack) # Requires both to be sets.
would be written as:
found = 0
for n in needles:
    if n in haystack:
        found += 1
Solution:
found = len(set(needles) & set(haystack))
Another way:
found = len(set(needles).intersection(haystack))
"""

# Set literals.
s = {1}
print(type(2))
print(s)
print(s.pop())
print(s)
dis("{1}")
dis("set([1])")

# Set comprehension.
# Setcomps.
# Build a set of characters with codes from 32 to 256 that have the
# word 'SIGN' in the name.
c = {chr(i) for i in range(32, 256) if "SIGN" in name(chr(i), "")}
print(c)
