# all come releted to Programiz --> https://www.programiz.com/python-programming/examples
# from sys import exc_info
from cmath import log
from functools import reduce
from itertools import count
from math import floor
import math
from random import random


class BasicAlgo():
    """
    Python Basic Logis and Methods
    =======================

    this is basic Logis class
    """

    def __init__(self, gNum1=0, gNum2=0):
        self.gNum1 = gNum1
        self.gNum2 = gNum2

    def add(self, lN1, lN2):
        return lN1 + lN2

    def oddNumber(self, lastNumber=None):
        return [oddN for oddN in range(0, lastNumber+1) if oddN % 2 == 1]

    def evenNumber(self, lastNumber=None):
        return [evenN for evenN in range(0, lastNumber+1) if evenN % 2 == 0]

    def sqrtN(self, lN1, lNpower=None):
        return lN1**lNpower

    def AreaOfTriangle(self, base=None, hieght=None):
        return (base*hieght) / 2

    def swapTwoValue(self, value1=None, value2=None):
        # using temp variable
        # temp = value1
        # value1 = value2
        # value2 = temp

        # using add and subtraction
        # value1 += value2
        # value2 = value1 - value2
        # value1 -= value2

        # using Multiplication and Division
        # value1 *= value2
        # value2 = value1 / value2
        # value1 /= value2

        # XOR swap  ==== conver in to bit then if 0 + 0 = 1, 1 + 1 = 1 ,0 + 1 = 0
        # value1 ^= value2
        # value2 = value1 ^ value2
        # value1 ^= value2

        # using reminder
        # value1, value2 = value2, value1

        # using tuple
        value1, value2 = value2, value1
        return int(value1), int(value2)

    def ganarateRandomNumber(self, limitNumber=10):
        return floor(random() * limitNumber)

    def converkiloMtoMile(self, km=None):
        # 1km == 0.621371ml, km/1.609 = ml
        return (km*0.621371)

    def celsiumToFahrenheit(self, cm=None):
        # (cm*9/5)+32 = F ,9/5 = 1.8
        return (cm*1.8) + 32

    def checkPositiveNegativeOrZero(self, Number=None):
        userNumber = float(input('Inter Number -> ')
                           ) if Number == None else Number
        # if Number == None:
        # Number = float(input('Inter Number -> '))
        return "Number is Positive" if userNumber > 0 else "Number is Zero" if userNumber == 0 else "Number is Negative"

    def checkLeepYearOrNot(self, year=None):
        userInputYear = int(input('Enter year -> ')) if year == None else year
        return f'{userInputYear} is not a leep year' if userInputYear % 4 != 0 else f'{userInputYear} is leep year' if userInputYear % 100 != 0 else f'{userInputYear} is leep year' if userInputYear % 400 == 0 else f'{userInputYear} is not a leep year'

    def largestNumberinArr(self, arr=None):
        userInputArr = input(
            'Enter Numbers -> ').split(" ") if arr == None else arr
        big = 0
        for item in userInputArr:
            if float(item) > float(big):
                big = item
        return big

    def findPrimeNumbers(self, number=None):
        userNumber = int(input('Enter number -> ')
                         ) if number == None else number  # input if None
        isDiv = False
        # checking
        for item in range(2, userNumber):
            if userNumber % item == 0:
                isDiv = True
                break
            else:
                isDiv = False
        div = [item for item in range(
            2, userNumber) if userNumber % item == 0]  # find divisible
        return f'{userNumber} is prime Number' if isDiv == False else f'{userNumber} is not prime Number divisible by {div}'

    def findAllPrimeNumberinRange(self, lastNumber=None):
        userNumber = int(input('Enter lastNumber -> ')
                         ) if lastNumber == None else lastNumber

        # return [item for item in range(2, userNumber) if userNumber % item != 0 else userNumber if userNumber % item == 0]
        temList = []
        for item in range(2, userNumber):
            for item2 in range(2, item):
                if item % item2 == 0:
                    break
                else:
                    temList.append(item)
                    break
        return temList

    def factorialNumber(self, number=None):
        userNumber = int(input('Enter lastNumber -> ')
                         ) if number == None else number
        if userNumber < 0:
            return 'Number no a Nagative'
        elif userNumber == 0:
            return 'the Factorila 0 is 1'
        else:
            factorila = 1
            for item in range(1, userNumber+1):
                factorila *= item
            return factorila

    def multiplicationTable(self, number=None):
        userNumber = int(input('Enter lastNumber -> ')
                         ) if number == None else number
        # temList = []
        for item in range(1, 11):
            # temList.append(f'{userNumber} x {item} = {userNumber*item}')
            print(f'{userNumber} x {item} = {userNumber*item}')
        # return temList

    # Python Program to Print the Fibonacci sequence
    def fibonacciSequence(self, number=None):
        a, b = 0, 1
        userNumber = int(input('Enter lastNumber -> ')
                         ) if number == None else number
        temList = []
        for item in range(0, userNumber):
            temList.append(a)
            a, b = b, a+b
        return(temList)

    # Python Program to Check Armstrong Number 121 == 121 <--revers
    def checkArmstrongNumber(self, number=None):
        userNumber = int(input('Enter lastNumber -> ')
                         ) if number == None else number
        tem = userNumber
        SumN = 0
        Number_len = len(str(tem))
        while tem > 0:
            reminder = tem % 10
            SumN += reminder**Number_len
            tem //= 10
        if SumN == userNumber:
            return f'{userNumber} is Armstrong Number'
        else:
            return f'{userNumber} is no Armstrong number'

    def findAllArmstrongNumber(self, startNumber=None, endNumber=None):
        temList = []
        for item in range(startNumber, endNumber+1):
            sum_Num = 0
            count = 0
            com_Number = item
            Number_len = len(str(item))
            while item > 0:
                reminder = item % 10
                sum_Num += reminder**Number_len
                item //= 10
                # if count == 10:
                #     break
                count += 1
            # print(sum_Num, com_Number)
            if sum_Num == com_Number:
                temList.append(sum_Num)
        return temList, count
    # Python Program to Find the Sum of Natural Numbers

    def naturalNumbers(self, number=None):
        userNumber = int(input('Enter lastNumber -> ')
                         ) if number == None else number
        # ==> see the full understating video https://www.youtube.com/watch?v=aaFrAFZATKU&t=115s
        return (userNumber*(userNumber+1))/2

    def power(self, arr=None):
        userArr = [1, 2, 3, 4, 5, 6, 7, 8, 9] if arr == None else arr
        return list(map(lambda x: x**2, userArr))

    # Python Program to Find Numbers Divisible by Another Number
    def numberDivisible(self, arr=None, divisibleNumber=None):
        # if function don't have paramiter
        userArr = [1, 2, 3, 4, 5, 6, 7, 8, 9] if arr == None else arr
        userDivisible = int(input('Enter number to divisible -> ')
                            ) if divisibleNumber == None else divisibleNumber
        return list(filter(lambda x: x % userDivisible == 0, userArr))

    # Python Program to Convert Decimal to Computer understand numbers -> (binary. Binary, octal and hexadecimal)
    def DecimalToCompUnderd(self, number=None):
        userNumber = int(input('Enter lastNumber -> ')
                         ) if number == None else number
        return (f'Your Decimal Number is {userNumber} Convert to \n\nBinary \t\t=> {bin(userNumber)}\nOctal \t\t=> {oct(userNumber)}\nHexadecimal \t=> {hex(userNumber)}')

    # Python Program to Find ASCII Value of Character
    def findAsccii(self, character=None):
        userCharacter = input('Enter Character -> ')
        return (f'Your Character is {userCharacter} and it\'s ASCII is {ord(userCharacter)} ')

    # Python Program to Find HCF or GCD
    def findLargestFector(self, number1, number2):
        # GCF = b%a = 0
        while number2:
            number1, number2 = number2, number1 % number2
        return number1


algo = BasicAlgo()
try:
    # print('add -> ', algo.add(1, 1))
    # print('power -> ', algo.sqrtN(4, 3))
    # print('oddNumber is -> ', algo.oddNumber())
    # print('oddNumber is -> ', algo.evenNumber(3, 6))
    # print('Area of triangle -> ', algo.AreaOfTriangle(6, 12))
    print('Swap Two value -> ', algo.swapTwoValue(5, 2))
    # print('Random Number -> ', algo.ganarateRandomNumber())
    # print('conver kilometre to mile -> ', algo.converkiloMtoMile(2))
    # print('celsium_to_fahrenheit -> ', algo.celsiumToFahrenheit(2))
    # print('Output -> ', algo.checkPositiveNegativeOrZero())
    # print('Output -> ', algo.checkLeepYearOrNot())
    # print('Output -> ', algo.largestNumberinArr())
    # print('Output -> ', algo.findPrimeNumbers())
    # print('Output -> ', range(2, math.floor(math.sqrt(10)+1)))
    # print('Output -> ', algo.findAllPrimeNumberinRange(10))
    # print('Output -> ', algo.factorialNumber())
    # algo.multiplicationTable()
    # print('output -> ', algo.fibonacciSequence())
    # print('Output -> ', algo.checkArmstrongNumber())
    # print('Output -> ', algo.findAllArmstrongNumber(100, 2000))
    # print('Output -> ', algo.naturalNumbers())
    # print('Output -> ', algo.power())
    # print('Output -> ', algo.numberDivisible())
    # print('Output -> ', algo.DecimalToCompUnderd())
    # print('Output -> ', algo.findAsccii())
    # print('Output -> ', algo.findLargestFector(24, 54))


# except:
#     print('Something went wrong', exc_info()[1])  # -> catch Error
except Exception as error:
    print('Something went wrong', error)  # -> catch Error
finally:
    print('\nThe try except is finished')
