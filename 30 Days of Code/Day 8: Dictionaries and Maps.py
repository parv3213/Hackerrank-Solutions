n = int(input())
i = 0
phoneBook = {}
for i in range(n):
    nameNumber = (input()).split()
    name = nameNumber[0]
    number = nameNumber[1]
    phoneBook[name] = number
try:
    while True:
        found = str(input())
        if found in phoneBook:
            print(found+"="+phoneBook[found])
        else:
            print("Not found")
except EOFError:
    pass
