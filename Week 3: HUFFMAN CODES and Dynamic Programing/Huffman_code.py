#In this programming problem and the next you'll code up the greedy algorithm from the lectures on Huffman coding.
#This file describes an instance of the problem. It has the following format:

#[number_of_symbols]

#[weight of symbol #1]

#[weight of symbol #2]

#...

#For example, the third line of the file is "6852892," indicating that the weight of the second symbol of the alphabet is 6852892. (We're using weights instead of frequencies, like in the "A More Complex Example" video.)

#Your task in this problem is to run the Huffman coding algorithm from lecture on this data set. What is the maximum length of a codeword in the resulting Huffman code?

#ADVICE: If you're not getting the correct answer, try debugging your algorithm using some small test cases. And then post them to the discussion forum!

def readfile():
	f = open("huffmanData.txt").read().split()[1:]
	arr = []
	for line in f:
		arr.append(int(line))
	return arr

class Node:
	def __init__(self,val=None, name = None):
		self.val = val
		self.left = None
		self.right = None
		self.parent = None
		self.name =  name


def merge(x,y):
	new_node = Node()
	new_node.val = x.val+y.val
	new_node.left = x
	new_node.right = y
	x.parent = new_node
	y.parent = new_node
	return new_node, x, y

def build_tree():
	arr = readfile()
	dic = {}
	for i in range(1000):
		dic[i]=1

	nodes = []
	temp_nodes = [Node(arr[i], i) for i in range(len(arr))]
	temp_nodes.sort(key = lambda x: x.val)
	while len(temp_nodes)>1:
		new_node, temp_nodes[0], temp_nodes[1] = merge(temp_nodes[0], temp_nodes[1])

		if temp_nodes[0].name in dic:
			nodes.append(temp_nodes[0])
		if temp_nodes[1].name in dic:
			nodes.append(temp_nodes[1])

		temp_nodes[1] = new_node
		temp_nodes.pop(0)
		temp_nodes.sort(key = lambda x: x.val)

	depth_arr = []
	for i in nodes:
		if i.left==None and i.right==None:
			temp = i
			depth = 0
			while temp.parent!=None:
				depth+=1
				temp = temp.parent
			depth_arr.append(depth)
	depth_arr.sort()
	return depth_arr
print(build_tree())
