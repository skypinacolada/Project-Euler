'''
You are given the following information, 
but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September, April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4,
 but not on a century unless it is divisible by 400.


How many Sundays fell on the first of the month during the twentieth century 
(1 Jan 1901 to 31 Dec 2000)?
'''

ordinary = [3, 0, 3, 2, 3, 2, 3, 3, 2, 3, 2, 3]
leap = [3, 1, 3, 2, 3, 2, 3, 3, 2, 3, 2, 3]


def counting_sundays():
    sunday_cnt = 0
    day = 2
    for year in range(1901, 2001):
        if year%4 ==0 : 
            months = leap
        else : 
            months = ordinary
        for day_plus in months:
            day += day_plus
            if day%7 == 0: sunday_cnt += 1
    return sunday_cnt


print(counting_sundays())