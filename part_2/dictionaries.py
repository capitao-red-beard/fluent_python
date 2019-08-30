import sys
import re
from collections import Counter, UserDict
from types import MappingProxyType


# Different ways to create a dictionary and comparison.
a = dict(one=1, two=2, three=3)
b = {"one": 1, "two": 2, "three": 3}
c = dict(zip(["one", "two", "three"], [1, 2, 3]))
d = dict([("two", 2), ("one", 1), ("three", 3)])
e = dict({"three": 3, "one": 1, "two": 2})
print(a == b == c == d == e)

# Dictionary comprehesnion.
# A list of pairs can be used directly with the dict constructor.
DIAL_CODES = [
    (86, "China"),
    (91, "India"),
    (1, "United States"),
    (62, "Indonesia"),
    (55, "Brazil"),
    (92, "Pakistan"),
    (880, "Bangladesh"),
    (234, "Nigeria"),
    (7, "Russia"),
    (81, "Japan"),
]
# Here the pairs are reversed: country is the key, code is the value.
country_code = {country: code for code, country in DIAL_CODES}
print(country_code)
# Reversing the keys again, values uppercased and items filtered by
# code < 66.
print({code: country.upper() for country, code in country_code.items() if code < 66})


# This class inherits from dict.
class StrKeyDict0(dict):

    # Check if key is already a str. If it is, and it's missing , raise
    # KeyError.
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]  # Build str from key and look it up.

    def get(self, key, default=None):
        try:
            # The get method delegates to __getitem__ by using
            # self[key] notation; that gives the opportunity for our
            # __missing__ to act.
            return self[key]
        except KeyError:
            # If KeyError was rasied, __missing__ already failed, so we
            # return the default.
            return default

    # Search for the unmodified key (the instance may contain non-str
    # keys), then for str built from the key.
    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()


# The __missing__ method.
d = StrKeyDict0([("2", "two"), ("4", "four")])
print(d["2"])
print(d["4"])
print(d.get("2"))
print(d.get("4"))
print(2 in d)
print(1 in d)

# Variations of dict.
# Counter holds an integer count for each key. Updating an existing key
# adds to its count. This can be used to count instances of hashable
# objects (the keys) or as a multiset-a set that holds several
# occurances of each element.
ct = Counter("abracadabra")
print(ct)
print(ct.most_common(2))


# StrKeyDict extends UserDict
class StrKeyDict(UserDict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    # We can assume all stored keys are str and we can check on
    # self.data instead of invoking self.keys().
    def __contains__(self, key):
        return str(key) in self.data

    # Converts any key to type str.
    def __setitem__(self, key, item):
        self.data[str(key)] = item


# Immutable mappings.
d = {1: "A"}
d_proxy = MappingProxyType(d)
print(d_proxy)
print(d_proxy[1])
