# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input().strip())
X = list(map(int, input().rstrip().split()))
W = list(map(int, input().rstrip().split()))

totalUpper = 0
totalW = 0
for i in range(len(X)):
    totalUpper += X[i]*W[i]
    totalW += W[i]
reqNo = totalUpper/totalW
print(round(reqNo, 1))
