'''
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''


def is_palindrome(num):
    length = len(str(num))-1
    for i in range(0, length+1):
        if str(num)[i] != str(num)[length-i] : return False 
    return True


def maxi_tri_palindrome():
    maxi = 0
    for n1 in range(999, 100, -1):
        for n2 in range(999, 100, -1):
            if is_palindrome(n1*n2) and n1*n2 >= maxi : maxi = n1*n2
    return maxi


print(maxi_tri_palindrome())


