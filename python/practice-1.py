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

# count operations to obtain zero
# how may time to become zero
'''
num1, num2 = 10, 10
count = 0
while num1 and num2:
    if(num1 >= num2):
        num1 = num1-num2
    else:
        num2 = num2-num1
    count += 1
print(count)
'''
# nums = [1, 3, 1, 2, 4, 3]
# nums[i-2] == nums[i]
# nums[i-1] != nums[i]
# matrix = [
#     [1, 0, 0, 1, 0],
#     [0, 0, 1, 0, 1],
#     [0, 0, 0, 1, 0],
#     [1, 0, 1, 0, 1]
# ]
# 0 1 0 0 1 0 1 1 1 1 0 1 ==> 4x3
# 0 0 1 0 0 0 1 1 0 0 0 1 1 1 0 1 0 1 0 1 1 == 3x7
# matrix = [
#     [0, 1, 0],
#     [0, 1, 0],
#     [1, 1, 1],
#     [1, 0, 1]
# ]
matrix = [
    [0, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1],
    [0, 1, 0, 1, 0, 1, 1]
]

def ValidCorner(matrix: list) -> bool:
    rows_size = len(matrix)
    columns_size = len(matrix[0])
    temp = {}
    row = 0

    while row < rows_size:
        coun_one = matrix[row].count(1)
        if(coun_one <= 1):
            row += 1
            continue
        col = 0
        while col < columns_size:
            # one step over col

            k = col+1
            while k < columns_size:
                if(matrix[row][col] == 1 and matrix[row][k] == 1):
                    # print((row, col), (row, k))
                    if (col in temp and k in temp[col]):
                        # print('col -> ', col, temp, k)
                        return True
                    if(k in temp and col in temp[k]):
                        # print('k -> ', col, temp, k)
                        return True
                    if col not in temp:
                        temp[col] = set()
                    if k not in temp:
                        temp[k] = set()
                    temp[col].add(k)
                    temp[k].add(col)
                    # print('f -> ', temp)
                k += 1
            col += 1
        row += 1
    return False


print(ValidCorner(matrix))
