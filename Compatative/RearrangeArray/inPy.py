def rearrangeArray(arr: list) -> list:
    arrangedArray = []
    for index in range(0, len(arr)):
        arrangedArray.insert(index, arr[arr[index]])
    return arrangedArray


arr = [0, 5, 1, 2, 4, 3]
arr = [4, 3, 2, 1, 0]
# print(rearrangeArray(arr))
print(list(range(0, len(arr))))
