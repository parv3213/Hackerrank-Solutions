def print_rangoli(size):
    # your code goes here
    arr = []
    for i in range(size, 0, -1):
        startChar = i
        toPrint = ""
        for j in range(size*2 -1):
            if(j%2 == 0):
                if startChar <= size:
                    printIt = chr(startChar+96)
                    startChar += 1
            else: printIt = "-"
            toPrint += printIt
        revOrder = toPrint[len(toPrint)-1:0:-1]
        combined = revOrder+toPrint
        arr.insert(j, combined)
    sub = 2
    for i in range(len(arr)*2 -1):
        if (i < len(arr)):
            print (arr[i])
        else:
            print (arr[i-sub])
            sub += 2


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)