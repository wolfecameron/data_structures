
class implicitMinHeap:

	def __init__(self):
		self.heap = []
		

	#actual code for string method written in 'strHelper' method
	def __str__(self):
		print("ROOT NODE: %s" % (self.heap[0]))
		self.strHelper(0)
		return " "


	#pre: index starts at zero to print entire heap
	#prints parent and child nodes recursively
	def strHelper(self,index): 
		
		#finds both children of item at self.heap[index]
		child1 = 2*index+1
		child2 = 2*index+2

		if(child2 < len(self.heap) and child1 < len(self.heap)):
			print("PARENT: %s; CHILDREN: %s,%s" % (self.heap[index],self.heap[child1],self.heap[child2]))

			#recursive calls for both child nodes 
			self.strHelper(child1)
			self.strHelper(child2)

		elif(child2 >= len(self.heap) and child1 < len(self.heap)):
			print("PARENT: %s; CHILDREN: %s" % (self.heap[index],self.heap[child1]))

			#recursive calls for child1 node
			self.strHelper(child1)
		else:
			#only occurs if both children exceed size of heap
			return



	def peek(self): #returns element at the top of the heap (minimum element)
		if(len(self.heap) == 0):
			return "Error: No elements in heap."

		return self.heap[0] 

	def push(self,data): #pushes value onto min heap 
		
		if(len(self.heap) == 0):
			self.heap.append(data)
			return

		self.heap.append(data)
		ind = len(self.heap) #stores current index of node as it searches for correct position
		while(not(ind == 1)):
			#NOTE: stored index values are not zero based, otherwise finding parent will not work
			parInd = ind/2 #uses integer division to find parent in heap
			if(self.heap[parInd-1] > self.heap[ind-1]): 
				#performs a swap on elements
				#updates current index
				tmp = self.heap[parInd-1] 
				self.heap[parInd-1] = self.heap[ind-1]
				self.heap[ind-1] = tmp
				ind = parInd
			else:
				break #only breaks if element is already in the correct spot

		 

	#pops (and returns) minumum element from heap
	#adjusts nodes to maintain heap structure
	def pop(self):
		if(len(self.heap) == 0):
			print("Error: Heap contains no elements")
			return 

		data = self.heap[0] 
		
		ind = 0 #use non-zero based index to be consistent with push operation
		
		while(((2*ind) +1) < len(self.heap) -1): #ensures both children within list range
			child1 = (2*ind) + 1 
			child2 = (2*ind) + 2
			if(self.heap[child1] < self.heap[child2]):
				self.heap[ind] = self.heap[child1]
				ind = child1
			else:
				self.heap[ind] = self.heap[child2]
				ind = child2

		#must discard node that is taken out of tree
		del self.heap[ind]
		return data

#use all of this to quickly test features of the heap
if __name__ == "__main__":
	x = implicitMinHeap()
	x.push(15)
	x.push(12)
	x.push(50)
	x.push(2)
	x.push(7)
	x.push(3)
	x.push(40)
	x.push(70000)

	print(x.peek())
	raw_input()
	print(x)
