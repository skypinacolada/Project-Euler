'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''


def is_prime(num, primes):
    for n in primes:
        if num%n==0 : return False 
    return True


def prime_under(maxi):
    primes = [2, 3]
    n = 3
    while (n < maxi):
        n += 2
        if is_prime(n, primes): primes.append(n)
    return primes


def change_to_square(li, maxi):
    for i, n in enumerate(li):
        sq = 1
        while(n**sq <= maxi):
            li[i] = n**sq
            sq += 1
    return li


def smallest_divisible(li):
    res = 1
    for n in li : res *= n
    return res 


print(smallest_divisible(change_to_square(prime_under(20), 20)))
