import numpy as np

orig_dim = np.array([5,4,3,2])
index_dim = np.array([5,4,3,2])

flag = True
count = 0
while flag:
    print orig_dim-index_dim
    count += 1
    l =  index_dim.shape[0]
    curr_index = l-1
    while curr_index >= 0:
        if index_dim[curr_index] > 0:
            index_dim[curr_index] -= 1
            break
        else:
            index_dim[curr_index] = orig_dim[curr_index]
        curr_index -= 1
    if curr_index < 0:
        break

print count
            

