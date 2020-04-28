def problem1():
	f = open("greedyJob.txt")
	arr = []
	for line in f:
		if len(line.split())==1:
			arr.append(line.split())
		else:
			temp_arr = line.split()
			arr.append([int(temp_arr[0]), int(temp_arr[1])])

	len_arr = int(arr[0][0])
	arr.pop(0)
	arr.sort(key = lambda x: (x[0]-x[1], x[0]), reverse=True)

	count=0
	sum1=0
	for i in arr:
		count+=i[1]
		sum1+=i[0]*count
	return sum1

def problem2():
	f = open("greedyJob.txt")
	arr = []
	for line in f:
		if len(line.split())==1:
			arr.append(line.split())
		else:
			temp_arr = line.split()
			arr.append([int(temp_arr[0]), int(temp_arr[1])])

	len_arr = int(arr[0][0])
	arr.pop(0)
	arr.sort(key = lambda x: x[0]/x[1], reverse=True)

	count=0
	sum1=0
	for i in arr:
		count+=i[1]
		sum1+=i[0]*count
	return sum1

# print(problem1())
# print(problem2())

def readPrimeData():
	file = open("Prime_edges.txt")
	arr =[]
	for line in file:
		temp_arr = line.split()
		if len(temp_arr)==2:
			arr.append([int(temp_arr[0]), int(temp_arr[0])])
		else:
			arr.append([int(temp_arr[0]), int(temp_arr[1]), int(temp_arr[2])])

	num_vertices = arr[0][0]
	num_edges = arr[0][1]
	arr.pop(0)
	return arr, num_vertices, num_edges

def primeAlgo():
	arr, num_vertices, num_edges = readPrimeData()
	pass_vertices = {}
	remaining_vertices = []

	for i in range(1, 501):
		pass_vertices[i]=0
		remaining_vertices.append(i)

	result = 0

	arr.sort(key = lambda x: x[2])

	pass_vertices[arr[0][0]]=1
	pass_vertices[arr[0][1]]=1
	remaining_vertices.remove(arr[0][0])
	remaining_vertices.remove(arr[0][1])
	result+=arr[0][2]

	count = 498
	while count>0:
		temp = []
		for i in arr:
			if (pass_vertices[i[0]]==1 and pass_vertices[i[1]]==0) or (pass_vertices[i[0]]==0 and pass_vertices[i[1]]==1):
				temp = i
				break
		if pass_vertices[temp[0]]==1:
			pass_vertices[temp[1]]=1
			result+=temp[2]
			remaining_vertices.remove(temp[1])
			count-=1
		elif pass_vertices[temp[1]]==1:
			pass_vertices[temp[0]]=1
			result+=temp[2]
			remaining_vertices.remove(temp[0])
			count-=1
	return result
print(primeAlgo())











