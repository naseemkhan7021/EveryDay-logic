print("i am a \\n this is ")  # output --> i am a \n this is
# a,b,c = [int(i) for i in input('enter number').split(',')] # this is list coprehancive method
# print(f'the averat of your enter three number is {(a+b+c)/3}') # this is string formating
# user_input = int(input('enter how many row you want  -> '))
# for i in range(0,user_input+1):
#     print('*'*i)
# *
# **
# ***
# ****
# *****

# for i in range(0,user_input+1):
#     for space in range(user_input-i,0,-1):
#         print(' ',end='')
#     print('*'*i,end='')
#     for nextStar in range(user_input-i,user_input+1):
#         print('*',end='')

# print()
#       *
#      ***
#     *****
#    *******
#   *********
#  ***********
# *************


# *******
# *     *
# *     *
# *******
# user_row = int(input(' enter number of row -> '))
# user_column = int(input(' enter number of column -> '))
# for column in range(1,user_column+1):
#     for row in range(1,user_row+1):
#         if row==1 or row==user_row or column==1 or column==user_column:
#             print('*',end='')
#             continue
#         print(' ',end='')

#     print()


#       *
#      0 *
#     0   *
#    0     *
#   0       *
#  0         *
# 012345*******
# for i in range(0,user_input+1):
#     for space in range(user_input-i,0,-1):
#         print(' ',end='')
#     for firstStar in range(0,i):
#         if firstStar==0 or i==user_input:
#             print('*',end='')
#             continue
#         print(' ',end='')
#     for nextStar in range(user_input-i,user_input+1):
#         if nextStar==user_input or i==user_input:

#             print('*',end='')
#             continue
#         print(' ',end='')

#     print()

# Find the missing number of given array in out of 10
# num10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# arr = [4, 2, 6, 9]
# notMatch = []
# match ---> modify the main list
# for item in num10:
#     for item2 in arr:
#         if item == item2:
#             num10.remove(item)

# not match ---> use new list for not matching element
# for item in range(1, 11):
#     notSatisfy = False
#     for item2 in arr:
#         if item == item2:
#             notSatisfy = False
#             break
#         else:
#             notSatisfy = True
#     if notSatisfy:
#         notMatch.append(item)
# print(notMatch)

# -------------------------------------
# count latter more then 2
# thisString = "naseeeeem"
# count = 0
# for i in range(1, len(thisString)-1):
#     if thisString[i] == thisString[i-1] and thisString[i] == thisString[i+1]:
#         count += 1
# print(count)

# -------------------------------------
# count latter more then 2
s = 'naseem'
t = 'salman'
