binary_array=[1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0]
i=0
j=len(binary_array)-1
while (i<=j):
    if binary_array[i]==1:
        if binary_array[j]==0:
            binary_array[i]=0
            binary_array[j]=1
        else: j-=1
    else: i+=1
print (binary_array)