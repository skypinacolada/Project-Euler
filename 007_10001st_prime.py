'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
we can see that the 6th prime is 13.

What is the 10001st prime number?
'''

def is_prime(num, li):
    for n in li:
        if num % n == 0 : return False
    return True


def nth_prime(goal):
    primes = [2, 3, 5]
    num = 5
    while (len(primes) < goal):
        num += 2
        if str(num)[-1] != 5 and is_prime(num, primes): primes.append(num)
    print(primes)
    return primes[-1]


print(nth_prime(10001))