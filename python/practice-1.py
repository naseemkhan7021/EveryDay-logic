# this exercie from w3resource.come
# print('Twinkle, twinkle, little star,\n\t How I wonder what you are!\n\t\t Up above the world so high,\n\t\t Like a diamond in the sky.\n Twinkle, twinkle, little star,\n\t How I wonder what you are!')
# output:
# Twinkle, twinkle, little star,
#          How I wonder what you are!
#                  Up above the world so high,
#                  Like a diamond in the sky.
#  Twinkle, twinkle, little star,
#          How I wonder what you are!
# find python_version
'''
import platform
print(platform.python_branch())  # tags/v3.8.3
# ('tags/v3.8.3:6f8c832', 'May 13 2020 22:20:19')
print(platform.python_build())
print(platform.python_compiler())  # MSC v.1925 32 bit (Intel)
print(platform.python_implementation())  # CPython
print(platform.python_revision())  # 6f8c832
print(platform.python_version())  # 3.8.3
print(platform.python_version_tuple())  # ('3', '8', '3')
'''

# another way to find python version
''' 
import sys
print(sys.version)
print(sys.version_info)
print(sys.api_version)
print(sys.last_value)
'''

# this is date time formate
'''
from datetime import datetime
# print(datetime.today() )
today = datetime.today()
# today.strftime => date to string date 
# today.strptime => string to date 
print(today.strftime("%Y-%b-%d %H:%M:%S"))
'''

'''
import math
radios = float(input('inter the circule radios -> '))
print(f'area of circul is {math.pi*(radios**2)}')
'''

# reverse the name of user input
# name = input('Enter you name -> ')
# rname = reversed(name)
# print(rname)

# print list and tuple
'''
listIs = [int(i) for i in input('enter number -> ').split(',')]
print(listIs)
print(tuple(listIs))
'''

# print file extension
'''
fileName = input('Enter file name -> ')
print(fileName.strip('.')) # use of strip is remove any character if precent in string
filname,ext = fileName.split('.')
print(f'filename:- {filname}\nextension:- {ext}')
'''

# print first and last color from following list
'''
color_list = ["Red","Green","White" ,"Black"]
print(f'first_color:- {color_list[0]}\nlast_color:- {color_list[-1]}')
'''
'''
date formating
exam_st_date = (11, 12, 2014)
print(f'{exam_st_date[0]}/{exam_st_date[1]}/{exam_st_date[2]}')
print('%i/%i/%i'%exam_st_date)
'''
# sum of same string number by using eval function and format function
'''
n = int(input('Enter number :- '))
print(eval('{0}+{0}{0}+{0}{0}{0}'.format(n)))
'''

# print __doc__ of function
# print(abs.__dir__)
# print(list.__doc__)

# print tha calendar of given month and year
'''
import calendar
print(calendar._nextmonth(2021, 1))
print(calendar.month(2021, 2))
'''
