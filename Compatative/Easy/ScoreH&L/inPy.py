scores = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]


def breakingRecords(scores):
    # Write your code here
    count_high_low = [0, 0]
    high, low = scores[0], scores[0]
    for index in range(0, len(scores)-1):
        if(scores[index] > scores[index+1]):
            if (low > scores[index+1]):
                low = scores[index+1]
                count_high_low[1] += 1
        elif scores[index] < scores[index+1]:
            if (high < scores[index+1]):
                high = scores[index+1]
                count_high_low[0] += 1
    return count_high_low


print(breakingRecords(scores))
