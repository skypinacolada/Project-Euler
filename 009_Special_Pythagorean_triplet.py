'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a**2 + b**2 = c**2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

def find():
    a = 1
    while (a <= 332):
        b = 2
        while (b < 1000-a-b):
            if a**2+b**2 == (1000-a-b)**2: return (a*b*(1000-a-b))
            b += 1
        a += 1

print(find())
