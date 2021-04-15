'''
2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?
'''

import datetime
start = datetime.datetime.now()


def summa():
    res = 0 
    for i in str(2**1000):res += int(i)
    return res 


print(summa())
print(datetime.datetime.now() - start)
#0.0002
