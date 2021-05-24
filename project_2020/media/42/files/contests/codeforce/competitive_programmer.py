import math
from itertools import permutations

def magic(numList):
    s = map(str, numList)
    s = ''.join(s)
    s = int(s)
    return s

def str_list(list1):
    lis=[]
    for i in list1:
        lis.append(magic(list(i)))
    return lis

def re_arrange(num):
    for i in num:
        if int(i)==0:
            i=0
        a=list(permutations([int(d) for d in str(i)]))
        a=str_list(a)
        count=0
        for j in a:
            if j%60==0:
                count +=1
        if count>0:
            print('red')
        else:
            print('cyan')

if __name__ == '__main__':
    num = []
    n=int(input())

    for i in range(n):
        a=input()
        num.append(a)

    re_arrange(num)
