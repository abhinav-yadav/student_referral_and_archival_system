def check(num1,num2):
    for i in range(1,7):
        if num1==(num2*14)+i:
            return num1
    return -1

def tower(pips):
    a=[]
    for i in pips:
        a.append(i//14)
    for i in range(len(pips)):
        if pips[i]==check(pips[i],a[i]):
            print('YES')
        else:
            print('NO')

if __name__=='__main__':
    a=int(input())
    b=list(map(int, input().rstrip().split()))
    tower(b)
