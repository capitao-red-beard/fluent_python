from array import array
from random import random
from collections import deque


# Create an array of double precision floats.
floats = array("d", (random() for i in range(10 ** 7)))
# Inspect the last number in the array.
print(floats[-1])
# Save the array to a binary file.
fp = open("floats.bin", "wb")
floats.tofile(fp)
fp.close()
# Create an empty array of doubles.
floats2 = array("d")
fp = open("floats.bin", "rb")
# Read 10 million numbers from the binary file.
floats2.fromfile(fp, 10 ** 7)
fp.close()
# Inspect the last number in the array.
print(floats2[-1])
# Verify the contents of the arrays match.
print(floats2 == floats)

# Memory Views.
numbers = array("h", [-2, -1, 0, 1, 2])
# Build memory view from array of short 5 signed integer (typecode 'h').
memv = memoryview(numbers)
print(len(memv))
# memv sees the same 5 intems in the array.
print(memv[0])
# Create a memv_oct by casting the elements of memv to typecode 'B'
# (unsigned char).
memv_oct = memv.cast("B")
# Export elements of memv_oct as as list, for inspection.
print(memv_oct.tolist())
# Assign value 4 to byte offset 5.
memv_oct[5] = 4
print(numbers)

# Dequeues and other queues.
# Optional maxlen argument sets the max no. of arguments allowed in
# this instance of queue; this sets a read-only maxlen instance
# attribute.
dq = deque(range(10), maxlen=10)
print(dq)
# Rotating with n > 0 takes items from the right end and prepends them
# to the left; when n < 0 items are taken from the left and appended to
# the right.
dq.rotate(3)
print(dq)
dq.rotate(-4)
print(dq)
# Appending to a dequeue that is full (len(d) == d.maxlen) discards
# items from the other end; note in the next line the 0 is dropped.
dq.appendleft(-1)
print(dq)
# Adding three items to the right pushes out the left most -1, 1, and 2.
dq.extend([11, 22, 33])
print(dq)
# Note that extendleft(iter) works by appending each successive item of
# the iter argument to the left of the dequeue, therefore the final
# position of the items is reversed.
dq.extendleft([10, 20, 30, 40])
print(dq)
