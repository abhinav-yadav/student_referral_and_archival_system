def check(lis):
    count=len(lis)*len(lis[0])
    for i in range(len(lis)):
        for j in range(len(lis[0])):




if __name__=='__main__':
    N=int(input())
    a=[]
    for i in range(N):
        a.append([])
        n,m=map(int,input().split())
        for j in range(n):
             a[i].append(list(map(int,input().split())))
    t=[]
    for i in a:
        t.append(check(i))
    for i in t:
        print(i)
