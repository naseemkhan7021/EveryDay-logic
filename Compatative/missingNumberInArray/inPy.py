# Find the missing number of given array in out of 10
num10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr = [4, 2, 6, 9]
notMatch = []
# match ---> modify the main list
for item in num10:
    for item2 in arr:
        if item == item2:
            num10.remove(item)

# not match ---> use new list for not matching element
for item in range(1, 11):
    notSatisfy = False
    for item2 in arr:
        if item == item2:
            notSatisfy = False
            break
        else:
            notSatisfy = True
    if notSatisfy:
        notMatch.append(item)
print(notMatch)
