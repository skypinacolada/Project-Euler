'''
the difference between the sum of the squares of the first ten natural numbers and the square of the sum is.

3025 - 385 = 2640

Find the difference between the sum of the squares of the first one hundred natural numbers 
and the square of the sum.
'''


import datetime
start = datetime.datetime.now()


def sum_of_the_squares(mini, maxi):
    res = 0
    for n in range(mini, maxi+1):
        res += n**2
    return res 


def square_of_the_sum(mini, maxi):
    return (int((mini+maxi)*(maxi-mini+1)/2))**2


print(square_of_the_sum(1, 100)-sum_of_the_squares(1, 100))
print(datetime.datetime.now() - start)
#0.0001s