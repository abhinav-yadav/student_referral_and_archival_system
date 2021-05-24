def tower(pips):
    for i in pips:
        for j in range(1,7):
            if (i-j)%14==0:
                print('YES')
                a=0
                break
        if a==0:
            a=1
            continue
        else:print('NO')

if __name__=='__main__':
    a=int(input())
    b=list(map(int, input().rstrip().split()))
    tower(b)
