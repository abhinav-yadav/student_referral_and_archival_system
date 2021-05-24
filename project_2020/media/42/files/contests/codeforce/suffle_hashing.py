from itertools import permutations

def shuffle(str,hash):
    for i in range(len(str)):
        if len(str[i])<10:
            perm_list = list(permutations(str[i]))
        else:
            perm_list=list(str[i])
        for j in perm_list:
            sub=hash[i].find((''.join(j)))
            if sub==-1:
                continue
            else:
                print('YES')
                break
        if sub == -1:
            print('NO')

if __name__ == '__main__':
    str=[]
    hash=[]
    n=int(input())
    for i in range(n):
        str.append(input())
        hash.append(input())
    shuffle(str,hash)
