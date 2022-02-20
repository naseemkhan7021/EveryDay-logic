# 12 to 24 hource
def timeConversion(s: str) -> str:
    # Write your code here
    arr = s.split(":")
    if(arr[-1][-2] == "A"):
        if(arr[0] == "12"):
            arr[0] = "00"
    else:
        if(arr[0] == "12"):
            arr[0] = "12"
        else:
            arr[0] = str(12+int(arr[0]))

    arr[-1] = arr[-1][:2]  # remove AM PM
    return ":".join(arr)


print(timeConversion("01:05:45PM"))
