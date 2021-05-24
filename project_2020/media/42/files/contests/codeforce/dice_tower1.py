def tower(pips):
    for i in pips:
        if i%14>0 and i%14<=6 and i>14:
            print("YES")
        else:
            print("NO")

if __name__=='__main__':
    a=int(input())
    b=list(map(int, input().split()))
    tower(b)
