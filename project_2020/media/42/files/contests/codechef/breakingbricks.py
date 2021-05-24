#      https://www.codechef.com/JAN20B/problems/BRKBKS
def recur(l):
    if l[0]==1:
        return(sum(l[1:]))
    elif l[1]+l[2]<=l[0] or l[3]+l[2]<=l[0]:
        return(2)
    elif l[1]+l[2]>l[0] or l[3]+l[2]>l[0]:
        return(3)

def brickbreak(lis):
    res=[]
    for i in lis:
        if sum(i[1:])<=i[0]:
            res.append(1)
        else:
            res.append(recur(i))
    return(res)

if __name__=='__main__':
    n=int(input())
    a=[]
    for i in range(n):
        a.append(list(map(int,input().split())))
    result=brickbreak(a)
    for i in result:
        print(i)
