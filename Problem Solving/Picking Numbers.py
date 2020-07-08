def pickingNumbers(a):
    # Write your code here
    maxReqSize = 0
    for num in a:
        reqSize = 0
        for subNum in a:
            sub = num - subNum
            if sub <= 1 and sub >= 0:
                reqSize += 1
        # print(num, subNum, reqSize)
        if (reqSize > maxReqSize):
            maxReqSize = reqSize
    return maxReqSize


n = int(input().strip())
a = list(map(int, input().rstrip().split()))
result = pickingNumbers(a)
print(result)
