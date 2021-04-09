'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
we can see that the 6th prime is 13.

What is the 10001st prime number?
'''

def is_prime(num):
    for n in range(2, int(num**(1/2))+1):
        if num % n == 0 : return False
    return True


def nth_prime(goal):
    cnt = 2
    num = 3
    while (cnt<goal):
        num += 2
        if is_prime(num): cnt += 1
    return num


print(nth_prime(10001))