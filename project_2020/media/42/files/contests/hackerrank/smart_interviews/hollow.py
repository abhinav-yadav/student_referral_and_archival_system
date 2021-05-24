def binary(lis,key,low,heigh):
    mid=(low+heigh)//2
    if(lis[mid]== key):
        return 'True'
    elif(lis[mid]>key):
        binary(lis,key,low,mid-1)
    elif (lis[mid]<key):
        binary(lis,key,mid+1,low)
    else:
        return 'False'

def merge(lis):
    if(len(lis)>1):
        mid=len(lis)//2
        left=lis[:mid]
        right=lis[mid:]
        merge(left)
        merge(right)

        l=0
        r=0
        c=[]
        while(len(left)-1>l and len(right)-1>r):
            if(left[l]>right[r]):
                c.append(right[r])
                r += 1
            else:
                c.append(left[l])
                l += 1
        while(len(left)-1>l):
            c.append(left[l])
            l += 1
        while(len(right)-1>r):
            c.append(right[r])
            r += 1

        return(c)


if __name__=='__main__':
    n=int(input())
    k=[]
    lis=[]
    for i in range(n):
        x,z=map(int,input().split())
        k.append(z)
        lis.append(list(map(int,input().split())))
    for i in range(n):
        lis[i]=merge(lis[i])
    for i in range(n):
        for j in lis[i]:
            a=k[i]-j
            if(binary(lis[i],a,0,len(lis[i]))):
                print('True')
            else:
                print('False')

        
