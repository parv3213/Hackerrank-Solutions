if __name__ == '__main__':
    names = []
    scores= []
    requiredArr = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        names.append(name)
        scores.append(score)

    minEl = min(scores)
    secMinEL = float("inf")
    for i in scores:
        if i > minEl:
            if i < secMinEL:
                secMinEL = i

    for i in range(len(scores)):
        if scores[i] == secMinEL:
            requiredArr.append(names[i])
    
    requiredArr.sort()
    for i in requiredArr:
        print (i)