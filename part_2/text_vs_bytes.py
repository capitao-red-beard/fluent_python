import array
import struct
import os
import sys
import locale


# Character issues.
# 4 unicode characters.
s = "café"
print(len(s))
# Encode str to bytes using UTF-8 encoding.
b = s.encode("utf-8")
# bytes literals start with b prefix.
print(b)
# bytes b has 5 bytes (the code point for "é" has two bytes in UTF-8).
print(len(b))
# Decode bytes to str using UTF-8 encoding.
print(b.decode("utf-8"))

# Byte essentials.
# bytes can be built from str, given an encoding.
cafe = bytes("café", encoding="utf_8")
print(cafe)
# Each item is in an interger in rage(256).
print(cafe[0])
# Slices of bytes are also bytes-even slices of single byte.
print(cafe[:1])
# There is no literal syntax for bytearray: they are shown as
# bytearray() with a byes literal as argument.
cafe_arr = bytearray(cafe)
print(cafe_arr)
# A slice of bytearray is also bytearray.
print(cafe_arr[-1:])
print(bytes.fromhex("31 4B CE A9"))

# Initializing bytes from the raw data of an aray.
# Typecode 'h' creates an array of short integers (16 bits).
numbers = array.array("h", [-2, -1, 0, 1, 2])
# octets holds a copy of the bytes that make up numbers.
octets = bytes(numbers)
# These are the 10 bytes that represent the five shortest integers.
print(octets)

# Basic encoders/decoders.
# codecs = encoders/decoders.
for codec in ["latin_1", "utf_8", "utf_16"]:
    print(codec, "El Nino".encode(codec), sep="\t")

# Understanding encode/decode problems.
# UnicodeEncodeError (when converting str to binary sequences).
city = "São Paulo"
# The 'utf_?' handle any str.
city.encode("utf_8")
city.encode("utf_16")
# This also works for the 'São Paulo' str.
city.encode("iso8859_1")
# Can't ensocde 'ã'. The default error handler-'strict'-raises
# UnicodeEncodeError.
# The ignore handler skips the character, bad idea.
city.encode("cp437", errors="ignore")
# When encoding replace handler substitutes encodable character with ?
# users will know somrthing is amiss.
city.encode("cp437", errors="replace")
# Replaces uncodeable charaters with an XML entity.
city.encode("cp437", errors="xmlcharrefreplace")

# UnicodeDecodeError (when reading binary sequences into str).
# These bytes are the characters for "Montréal" encoded as latin1;
# '\xe9' is the byte for "é".
octets = b"Montr\xe9al"
# Decoding works because because it is a proper subset of latin1.
octets.decode("cp1252")
# Is intended for Greek, so the '\xe9' byte is misenterpreted, no error.
octets.decode("iso8859_7")
# Is for Russian. Different character encoding for the special symbol.
octets.decode("koi8_r")
# 'utf_8' detects that octets is not valid UTF-8 and raises error.
# Using replace we set the value to '?'.
octets.decode("utf_8", errors="replace")

# Handling text files.
fp = open("cafe.txt", "w", encoding="utf_8")
# open operates on the text mode and returns TextIOWrapper object.
print(fp)
# The write method on a TextIOWrapper returns the number of unicode
# characters written.
print(fp.write("café"))
fp.close()
# os.stat reports that the file holds 5 bytes.
print(os.stat("cafe.txt").st_size)
# Opening a text file with no explicit encoding returns a TextIOWrapper
# with the encoding set to the system default.
fp2 = open("cafe.txt")
print(fp2)
# Inspect the encoding default.
print(fp2.encoding)
print(fp2.read())
# Opening the same file with the correct encoding.
fp3 = open("cafe.txt", encoding="utf_8")
print(fp3.read())
# Opens a file for read in binary mode.
fp4 = open("cafe.txt", "rb")
print(fp4)
# Returns bytes as expected.
print(fp4.read())

# Encoding defaults: A madhouse.
expressions = """
        locale.getpreferredencoding()
        type(my_file)
        my_file.encoding
        sys.stdout.isatty()
        sys.stdout.encoding
        sys.stdin.isatty()
        sys.stdin.encoding
        sys.stderr.isatty()
        sys.stderr.encoding
        sys.getdefaultencoding()
        sys.getfilesystemencoding()"""

my_file = open("dummy", "w")

for expression in expressions.split():
    value = eval(expression)
    print(expression.rjust(30), "->", repr(value))

# I will come back to this chapter later as I do not feel it is so
# relevant to me right now.
