if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    pointArr = []
    for a in range(x+1):
        for b in range(y+1):
            for c in range(z+1):
                pointArr.append([a,b,c])
    totalArr = []
    for i in pointArr:
        total = 0
        for j in i:
            total += j
        if total != n:
            totalArr.append(i)
    print (totalArr)