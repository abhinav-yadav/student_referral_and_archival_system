def matrix(m,n):
    if(m==n==1):
        print(0)
    elif(m==1):
        for i in range (1,n+1):
            print(i+1,end=' ')
    elif(n==1):
        for i in range (1,n+1):
            print(i+1)
    else:
        for i in range(1,m+1):
            for j in range(n):
                print(i*(m+j),end=' ')
            print()

if __name__=='__main__':
    m,n=map(int,input().split())
    matrix(m,n)
