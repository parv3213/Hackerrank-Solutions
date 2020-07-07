# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
arr = list(map(int, input().split(" ")))
arr.sort()

elementSum = 0
maxCount = 0
maxCountNum = 0
for el in arr:
    elementSum += (el)
    count = arr.count(el)
    if count > maxCount:
        maxCountNum = el
        maxCount = count

mean = elementSum/n
print(mean)


median = 0
if n % 2 != 0:
    median = arr[int(n/2)]/2
else:
    median = (arr[int(n/2)]+arr[int(n/2)-1])/2
print(median)
print(maxCountNum)
