# Find rectangle with corners as 1

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
                k += 1
            col += 1
        row += 1
    return False


print(ValidCorner(matrix))
