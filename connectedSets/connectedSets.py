# Enter your code here. Read input from STDIN. Print output to STDOUT
import traceback,random
#totalNumberOfInput=int(raw_input())
totalNumberOfInput=1
i=0
matrix=[]
dim=30

def findConnectedSet(cellArray):
	#keywords

	def isThisSet(cell):

		if cell % dim == 0:
			direction=[cell-dim+1,cell-dim,cell-dim+1,cell+1,cell+dim,cell+dim+1]
		elif (cell + 1) % dim == 0:
			direction=[cell-dim-1,cell-dim,cell-1,cell+dim,cell+dim-1]
		else:
			direction=[cell-dim-1,cell-dim,cell-dim+1,cell-1,cell+1,cell+dim-1,cell+dim,cell+dim+1]
		print cell
		print direction
		cellArray.remove(cell)
		for dirc in direction:
			if dirc in cellArray:
				isThisSet(dirc)
	countOfConnectedSet=0
	i=0
	x=len(cellArray)
	while(1):
		try:
			if len(cellArray)==0 or i==x:
				break
			else:
				countOfConnectedSet+=1
				isThisSet(cellArray[i])
			i=i+1
		except:
			break
			pass
	print countOfConnectedSet

def doProcessing(matArray):
	# print matArray
	cellArray=[]
	for j in range(0,len(matArray)):
		if matArray[j]==1:
			cellArray.append(j)
	matArray=[]
	print cellArray
	print len(cellArray)
	findConnectedSet(cellArray)


# while(i < totalNumberOfInput):
# 	matrix.append(i)
# 	matrix[i]=[]
# 	indx=0
# 	k=0
# 	dim=int(raw_input())
# 	while(indx < dim):
# 		matrix[i].extend(raw_input().strip().split(" "))
# 		indx+=1
# 	for k in range(0,len(matrix[i])):
# 		matrix[i][k]=int(matrix[i][k])
#1018081
matrix=[]
for i in range(0,250000):
	matrix.append(random.randrange(0,2))
	i=i+1
doProcessing(matrix)
i+=1