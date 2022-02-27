# https://www.hackerrank.com/challenges/migratory-birds/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
# arr = [1, 1, 2, 2, 3]
arr = [1, 4, 4, 4, 5, 3]


def migratoryBirds(arr):
    dic = {}
    for i in range(1, 6):
        if i not in arr:
            continue
        else:
            dic[i] = arr.count(i)
    maxValue = max(dic.values())
    manum = []
    for key, value in dic.items():
        if value == maxValue:
            manum.append(key)

    return min(manum)

# def migratoryBirds(arr):
#     dic = {}
#     for i in arr:
#         if i not in dic:
#             dic[i] = 1
#         else:
#             dic[i] += 1
#     maxValue = max(dic.values())
#     return min([key for key in dic.keys() if dic[key] == maxValue])


print(migratoryBirds(arr))
