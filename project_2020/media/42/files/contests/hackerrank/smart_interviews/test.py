import numpy as np
arr1 = np.array([[5, 6, 9], [21 ,18, 27]])
arr2 = np.array([[15 ,33, 24], [4 ,7, 1]])
result  = arr1 + arr2
print("addition of two arrays is \n",result)
for i in range(len(result)):
    for j in range(len(result[0])):
        result[i,j]=(pow(result[i,j],1/2))    
print("\nResult array after calculating the square root of all elements\n")
print(result)
