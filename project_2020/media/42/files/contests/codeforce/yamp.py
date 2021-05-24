def check(lis):
    c=0
    for i in range(1,lis[0]+1):
        for j in range(1,lis[1]+1):
            if (str((i*j)+i+j) == str(i)+str(j)):
                c +=1
    return c


n=int(input())
m=[]
for i in range(n):
    m.append(list(map(int,input().split())))
c=[]
for i in m:
    c.append(check(i))
print(c)
