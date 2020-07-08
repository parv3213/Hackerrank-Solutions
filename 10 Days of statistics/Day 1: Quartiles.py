n = int(input().strip())
x = list(map(int, input().rstrip().split()))
x.sort()
# Median


def medianCal(x):
    n = len(x)
    if n % 2 != 0:
        return x[int(n/2)]
    else:
        return (x[int(n/2)-1] + x[int(n/2)])/2


median = (medianCal(x))
if n % 2 == 0:
    print(int(medianCal(x[slice(0, int(n/2))])))
    print(int(median))
    print(int(medianCal(x[slice(int(n/2), len(x))])))
else:
    print(int(medianCal(x[slice(0, int(n/2))])))
    print(int(median))
    print(int(medianCal(x[slice(int(n/2)+1, len(x))])))
