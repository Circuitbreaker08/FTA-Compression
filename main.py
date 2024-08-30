import sys

sys.set_int_max_str_digits(0)

with open("download.png", "rb") as f:
    data = f.read()

"""
print(bin(int.from_bytes(data)))
print("\n")
print(len(bin(int.from_bytes(data))))
print("\n\n\n\n\n")
print(int.from_bytes(data))
print("\n")
print(len(str(int.from_bytes(data))))
"""

def primes_gen(): #use yield
    pass

def is_prime(number) -> bool:
    pass

def compress(data):
    pass

def decompress(data):
    pass

compress(data)

#2322818
#699238