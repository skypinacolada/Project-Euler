'''
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''

import datetime
start = datetime.datetime.now()


def fac(num):
    if num == 1 : return 1
    return num*fac(num-1)


def sum_of_digits(num):
    res = 0 
    for n in str(num) : res += int(n)
    return res 


print(sum_of_digits(fac(100)))
print(datetime.datetime.now() - start)
#0.0001s