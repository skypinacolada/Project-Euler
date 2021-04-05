'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''


def sum_of_multiples(div1, div2, max):
    res = 0
    for num in range(1, max):
        if num%div1==0 or num%div2==0 : res += num
    return res

print(sum_of_multiples(3, 5, 10))
print(sum_of_multiples(3, 5, 1000))
