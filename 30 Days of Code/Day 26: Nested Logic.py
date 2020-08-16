returnDate = list(map(int, input().rstrip().split()))
dueDate = list(map(int, input().rstrip().split()))

differenceList = []

for i in range(3):
    difference = returnDate[i] - dueDate[i]
    differenceList.append(difference)

if (differenceList[2] > 0):
    print(10000)

elif(differenceList[1] > 0 and differenceList[2] == 0):
    print(differenceList[1]*500)

elif(differenceList[0] > 0 and differenceList[2] == 0 and differenceList[2] == 0):
    print(differenceList[0]*15)

else:
    print(0)
