
def maxList(listin):
    max = listin[0]
    for i in listin:
        if (i>max):
            max = i
    return max
def minList(listin):
    min = listin[0]
    for i in listin:
        if (i<min):
            min = i
    return min
def sumList(listin):
    sum = 0
    for i in listin:
        sum+=i
    return sum; 
def averageList(listin):
    return sumList(listin)/len(listin)
def medianList(listin):
    listin = sorted(listin)
    if (len(listin)%2==0):
        return ((listin[len(listin)//2]+listin[(len(listin)//2) - 1])/2)
    else:
        return listin[len(listin)//2]