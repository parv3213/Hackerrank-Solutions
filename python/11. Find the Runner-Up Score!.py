if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    maxEl = max(arr)
    for i in range(arr.count(maxEl)):
        arr.remove(maxEl)
    print (max(arr))
