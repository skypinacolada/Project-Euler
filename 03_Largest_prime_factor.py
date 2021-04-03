'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

import math

def is_prime(num):
    for i in range(2, num):
        if num%i==0 : return False
    return True


def factors(num):
    res = []
    half = math.floor(num/2)
    for i in range(2, half+1):
        if i in res: break
        if num%i==0:
            res.append(i)
            res.append(int(num/i))
    return res

def max_prime_factor(li):
    maxi = 0
    for n in li:
        if is_prime(n) and n >= maxi : maxi = n
    return maxi


print(max_prime_factor(factors(600851475143)))
