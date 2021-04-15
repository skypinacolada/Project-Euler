'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''


limit = 999

div_3 = limit//3
div_5 = limit//5
div_15 = limit//15

print(((div_3+1)*(div_3/2)*3) + ((div_5+1)*(div_5/2)*5) - ((div_15+1)*(div_15/2)*15))
