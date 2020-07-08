n = int(input())  # Take int from user
binaryNum = []


def decToBinary(num):
    if num > 1:
        decToBinary(num//2)
    binaryNum.append(num % 2)


decToBinary(n)

reqNo = 0
reqNoMax = 0
for count in range(len(binaryNum)):
    if(binaryNum[count] == 1):

        reqNo = 1
        count2 = count+1
        for count2 in range(count2, len(binaryNum)):
            if binaryNum[count2] == 1:
                reqNo += 1
            else:
                break
        if (reqNo > reqNoMax):
            reqNoMax = reqNo
        count = count2+1

print(reqNoMax)
