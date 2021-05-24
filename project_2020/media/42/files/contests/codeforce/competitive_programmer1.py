import math

def zero(lis):
    for i in lis:
        if i==0:
            return 'true'
    return 'false'

def even1(lis):
    count=0
    for i in lis:
        if i%2==0 :
            if i==0 and count==0:
                count +=1
            else:
                return 'true'
    return 'false'

def re_arrange(num):
    b=[]
    for i in num:
        if int(i)==0:
            i=0
        b.append(list(int(j) for j in str(i)))
    for i in b:
        if sum(i)%3==0 and zero(i)=='true' and  (even1(i)=='true' or (len(i)==1 and i[0]==0)):
            print('red')
        else:
            print('cyan')

if __name__=='__main__':
    num=[]
    for i in range (int(input())):
        j=input()
        num.append(j)
    re_arrange(num)
