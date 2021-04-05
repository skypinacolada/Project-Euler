'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''


def is_prime(num):
    for n in range(2, num):
        if num%n==0 : return False 
    return True


def prime_under(maxi):
    res = []
    for n in range(2, maxi+1):
        if is_prime(n): res.append(n)
    return res


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
