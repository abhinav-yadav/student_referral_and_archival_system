# https://codeforces.com/contest/1288/problem/A
import math
def check(lis):
    i=1
    print(lis)
    c='NO'
    while(i<lis[0]):
        if (i+math.ceil(lis[1]/(i+1))<=lis[0]):
            c='YES'
            break
        i +=1
    return c

n=int(input())
m=[]
for i in range(n):
    m.append(list(map(int,input().split())))
c=[]
for i in range(n):
    if (m[i][1]<=m[i][0]):
        c.append('YES')
    else:
        c.append(check(m[i]))
for i in c:
    print(i)
