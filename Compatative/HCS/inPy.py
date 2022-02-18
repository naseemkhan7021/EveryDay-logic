def HCF(number1, number2):
    while(number2):
        number1, number2 = number2, number1 % number2
    return number1


print(HCF(24, 54))
