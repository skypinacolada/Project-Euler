'''
Let d(n) be defined as the sum of proper divisors of n 
(numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, 
then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
 therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; 
 so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''

import datetime
start = datetime.datetime.now()


def d(n):
    res = 1
    for div in range(2, int(n/2)+1):
        if n%div == 0 : res += div
    return res


def amicable(a):
    b = d(a)
    if b <= a : return False
    if d(b) == a : return [a,b]
    return False


def sum_amicable(maxi):
    res = 0
    num_pool = list(range(2, maxi))
    for n in num_pool:
        ami = amicable(n)
        if type(ami) == list : 
            res += (ami[0] + ami[1])
            num_pool.remove(ami[1])
    return res
     

print(sum_amicable(10000))
print(datetime.datetime.now() - start)


'''
2s

더 최적화할 수 있을 것 같은데 안 보인다. 
앞으로는 늘 이렇게 시간을 재야겠다. 
'''
