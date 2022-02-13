#  find dublicat
sp_count = 0
dublicatArr = [3, 1, 3, 4, 2]
# dublicatArr_1 = [1, 3, 4, 2, 2]
# output ==> 2 , https://www.codingninjas.com/codestudio/problems/find-duplicate-in-array_1112602?leftPanelTab=1
for index_outer in range(0, len(dublicatArr)):
    for index_inner in range(index_outer+1, len(dublicatArr)):
        sp_count += 1
        print(sp_count)
        if(dublicatArr[index_outer] == dublicatArr[index_inner]):
            print(dublicatArr[index_outer])
        else:
            continue

print(sp_count)
