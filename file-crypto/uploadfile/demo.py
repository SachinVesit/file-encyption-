#python3
n = 0
def getlist():
    n = int(input())
    l = [int(j)  for j in input().split()]
    maxproduct(l)

def maxproduct(l):
    if len(l) > n:
        getlist()
    else:
        maxi = max(l)
        l.sort(reversed)
        length = len(l)
        temp = 0
        for i in range(0,length):
            if l[i] != maxi and l[i] < maxi :   
                temp = l[i]
        print(maxi * temp)
getlist()