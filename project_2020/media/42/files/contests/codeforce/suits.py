import math

a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
f=int(input())
d2=d

min1=min(a,d)
min2=min(b,c,d)
cost1=0
cost2=0

cost1 = min1*e
if min1 != d:
    d=d-min1
    cost1 += min(b,c,d)*f

cost2 = min2*f
if min2 != d2:
    d2=d2-min2
    cost2 += min(a,d2)*e

if cost1>cost2:
    print(cost1)
else:
    print(cost2)
