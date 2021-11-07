binary_array=[1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0]
starting_index=0
ending_index=len(binary_array)-1
while (starting_index<=ending_index):
    if binary_array[starting_index]==1:
        if binary_array[ending_index]==0:
            binary_array[starting_index]=0
            binary_array[ending_index]=1
        else: ending_index-=1
    else: starting_index+=1
print (binary_array)
