'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
Although it has not been proved yet (Collatz Problem), 
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''


import datetime
start = datetime.datetime.now()

chain = set()

def collatz(n):
    cnt = 1 
    while (n != 1):
        if n%2 == 0: 
            n = int(n/2)
        else:
            n = 3*n + 1
        chain.add(n)
        cnt += 1
    return cnt


def longest_chain(limit):
    maxi = 0 
    res = 0 
    for n in range(limit+1, 1, -2):
        if n in chain : continue 
        chain.add(n)
        c = collatz(n)
        if c > maxi : 
            maxi = c
            res = n
    return res


print(longest_chain(1000000))
print(datetime.datetime.now() - start)


'''
12sec
하트를 많이 받은 순으로 다른 답을 볼 수 있구나!

**a Better Solution**
한 체인 안의 수들은 같은 체인의 다른 부분집합을 내놓을 뿐이기 때문에 다시 체크하지 않아도 된다. 
'''
