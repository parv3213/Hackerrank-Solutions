# Enter your code here. Read input from STDIN. Print output to STDOUT
times = int(input())
for time in range(times):
    string = str(input())
    # print (string,time)
    str1 = ""
    str2 = ""
    i = 1
    for char in string:
        if i % 2 == 0:
            str2 += char
        else:
            str1 += char
        i += 1
    print(str1+" "+str2)
