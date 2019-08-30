from vector2d_v0 import Vector2d


# See vector2d_v0.py for the __slots__ explanation and implementation.
v1 = Vector2d(1.1, 2.2)
dumpd = bytes(v1)
print(dumpd)
# Default representation is 17 bytes long.
print(len(dumpd))
# Change the typecode to 'f' in instance v1.
v1.typecode = "f"
dumpf = bytes(v1)
print(dumpf)
# Representation is now 9 bytes long.
print(len(dumpf))
# Vector2d.typecode is unchanged, we only changed for the instance v1.
print(Vector2d.typecode)
