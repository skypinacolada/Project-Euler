'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

import datetime
start = datetime.datetime.now()

def is_prime(num):
    for div in range(2, int(num**(1/2))+1):
        if num%div==0 : return False
    return True


def factors(num):
    res = []
    half = int(num/2)
    for i in range(2, half+1):
        if i in res: break
        if num%i==0:
            res.append(i)
            res.append(int(num/i))
    return res


def max_prime_factor(li):
    li = sorted(li, reverse=True)
    for n in li:
        if is_prime(n) : return n

print(max_prime_factor(factors(600851475143)))
print(datetime.datetime.now() - start)

#0.6sec
