import itertools
def clustering(file_name):
	file = open(file_name)
	num_nodes = int(file.readline())
	arr = []
	for line in itertools.islice(file, 1, None):
		line = line.split()
		arr.append([int(line[0]), int(line[1]), int(line[2])])

	arr.sort(key = lambda x: x[2])
	num_cluster = num_nodes
	cluster = []
	for i in range(1, num_nodes+1):
		cluster.append([i])
	
	def findGroup(cluster, element):
		for i in range(len(cluster)):
			if element in cluster[i]:
				return i

	max_spacing = 0
	while num_cluster>3:
		# print(num_cluster)
		for i in arr:
			temp_x = findGroup(cluster, i[0])
			temp_y = findGroup(cluster, i[1])
			if temp_x!=temp_y:
				if num_cluster!=4:
					new_arr = cluster[temp_x]+cluster[temp_y]
					cluster[temp_x] = new_arr
					cluster.pop(temp_y)
					num_cluster-=1
					break
				else:
					max_spacing = i[2]
					num_cluster-=1
					break

	return max_spacing

# print(clustering("clustering.txt"))
#106
