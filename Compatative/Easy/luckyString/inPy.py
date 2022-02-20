# count latter more then 2
thisString = "naseeeeem"
count = 0
for i in range(1, len(thisString)-1):
    if thisString[i] == thisString[i-1] and thisString[i] == thisString[i+1]:
        count += 1
print(count)