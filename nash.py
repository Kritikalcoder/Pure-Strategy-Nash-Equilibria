#Display all nash equilibria of a n-person normal form game
# Pure strategy nash equilibria
import sys, os
import copy
import numpy as np
import math
input_f = sys.argv[1]

input_file = open(input_f, "r")
# with open(input_f, "r") as input_file:
line_no = 0
for line in input_file:
	line_no += 1
	if line_no == 1:
		continue
	elif line_no == 2:
		player_action_info = line.split()
	elif line_no == 3:
		continue
	else:
		util_list = line.split()

index = 0
players = []

# while player_action_info[index]!="}":
# 	print player_action_info[index]
# 	index+=1

# print 'DONE'


while player_action_info[index] != '}':
	index += 1
	# List of players
	# print player_action_info[index]
	if player_action_info[index] == "\"Player" or player_action_info[index] == "{" or player_action_info[index] == "}":
		continue
	else:
		# print player_action_info[index]
		players.append(int(player_action_info[index].strip('\"')))
# print players

player_count = len(players)
index += 2
action_counts = []
while player_action_info[index] != '}':
	# List of count of actions per player
	action_counts.append(int(player_action_info[index].strip()))
	index+=1
# action_counts_rev = action_counts.reverse()
action_counts_rev = copy.deepcopy(action_counts)
action_counts_rev.reverse()
# print action_counts

#########################################

tuple_dim_list = action_counts_rev + [player_count]
tup = tuple([t_count for t_count in tuple_dim_list])
util_matrix = np.ndarray(shape=tup, dtype=float, order='C')

#############################################

orig_dim = np.array(tuple_dim_list)-1
#print orig_dim
index_dim = copy.deepcopy(orig_dim)

flag = True
indx_count = 0
j=0
while flag:
    index = orig_dim-index_dim
    # print index
    util_matrix[tuple(index)] = util_list[j]
    j = j+1
    indx_count += 1
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

# print util_matrix[0,:,:]
# print util_matrix[:,0,:]
# print util_matrix[:,:,0]

# # first value in matrix
# counters = [0] * (player_count + 1)
# val = util_list[0]
# index_tup = tuple([count for count in counters])
# util_matrix[index_tup] = val

# for dim in tuple_dim_list.reverse():
# rev_dim_list = tuple_dim_list.reverse()
# for i in range(len(rev_dim_list)):
# 	counters[i] = 0
# 	for j in range
# 	if counters[i] < (rev_dim_list[i]-1):
# 		counters[i] += 1

#############################################

action_space_rev = np.array(action_counts_rev)-1
action_space = np.array(action_counts) - 1
index_space_rev = copy.deepcopy(action_space_rev)

flag = True					# Flag for iterating through all the states

# print action_space_rev
while flag:
    index = action_space_rev - index_space_rev
    nash_flag = 1
    for plr in range(player_count):
    	# print plr
    	# plr_index = np.insert(index, 0, plr)
    	plr_index = np.append(index, plr)
    	# print plr_index
    	# print util_matrix.shape
    	cur_util = util_matrix[tuple(plr_index)]
    	# print cur_util
    	act_index = copy.deepcopy(plr_index)
    	for act in range(action_space[plr]):
    		act_index[player_count - plr_index - 1] = act
    		if cur_util < util_matrix[tuple(act_index)]:
    			nash_flag = 0
    			break

    if nash_flag == 1:
    	result = index[::-1]
    	print result

    l =  index_space_rev.shape[0]
    curr_index = l-1
    while curr_index >= 0:
        if index_space_rev[curr_index] > 0:
            index_space_rev[curr_index] -= 1
            break
        else:
            index_space_rev[curr_index] = action_space_rev[curr_index]
        curr_index -= 1
    if curr_index < 0:
        break
