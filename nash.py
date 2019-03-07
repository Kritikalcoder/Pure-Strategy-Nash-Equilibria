#Display all nash equilibria of a n-person normal form game
# Pure strategy nash equilibria
import sys, os
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
print players

player_count = len(players)
index += 2
action_counts = []
while player_action_info[index] != '}':
	# List of count of actions per player
	action_counts.append(int(player_action_info[index].strip()))
	index+=1
action_counts.reverse()
print action_counts

tuple_dim_list = [player_count] + action_counts
tup = tuple([t_count for t_count in tuple_dim_list])
util_matrix = np.ndarray(shape=tup, dtype=float, order='C')

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



	
