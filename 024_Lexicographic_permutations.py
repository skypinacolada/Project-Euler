'''
A permutation is an ordered arrangement of objects. 
For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
If all of the permutations are listed numerically or alphabetically, 
we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 
0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''

import datetime
start = datetime.datetime.now()


digits = [0, 1, 2, 3, 4, 5, 6, 7, 8 ,9]


def fac(n):
    if n == 0 : return 1
    return n*fac(n-1)


def near_to_million():
    nearing = 0 
    res = ''
    for i in range(9, -1, -1):
        mul = 1
        while(nearing+mul*fac(i)<1000000) : mul += 1 
        mul -= 1
        nearing += mul*fac(i)
        res += str(digits[mul])
        digits.remove(digits[mul])
    return int(res)


print(near_to_million())
print(datetime.datetime.now() - start)
#0.0001s
