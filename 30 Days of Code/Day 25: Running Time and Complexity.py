times = int(input())


def checkPrime(num):
    if num <= 1:
        return "Not prime"
    elif num <= 3:
        return "Prime"
    elif (num % 2 == 0 or num % 3 == 0):
        return "Not prime"
    i = 5
    while(i*i <= num):
        if (num % i == 0 or num % (i+2) == 0):
            return "Not prime"
        i = i+6
    return "Prime"


for i in range(times):
    num = int(input())
    print(checkPrime(num))
