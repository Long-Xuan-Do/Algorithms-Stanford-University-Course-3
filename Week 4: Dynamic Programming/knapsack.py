#In this programming problem and the next you'll code up the knapsack algorithm from lecture.
#This file describes a knapsack instance, and it has the following format:

#[knapsack_size][number_of_items]

#[value_1] [weight_1]

#[value_2] [weight_2]

#...

#For example, the third line of the file is "50074 659", indicating that the second item has value 50074 and size 659, respectively.

#You can assume that all numbers are positive. You should assume that item weights and the knapsack capacity are integers.

def knapsack_small():
	knap_size = 10000
	num_item = 100
	v_i = []
	w_i = []

	f = open("knapsack.txt")
	for line in f:
		line=line.split()
		v_i.append(int(line[0]))
		w_i.append(int(line[1]))

	v_i[0]=0
	w_i[0]=0

	result_arr = [[0 for i in range(knap_size+1)] for i in range(num_item+1)]

	for i in range(0, num_item+1):
		for j in range(0, knap_size+1):
			if i==0 or j==0:
				result_arr[i][j]=0
			else:
				temp = j-w_i[i]
				if temp<0:
					result_arr[i][j] = result_arr[i-1][j]
				else:
					result_arr[i][j] = max(result_arr[i-1][j], result_arr[i-1][temp]+v_i[i])

	return result_arr[100][10000]

# print(knapsack_small())
#2493893
