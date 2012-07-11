import re
# mainStr="known as the 'Eternal City', Rome is the capital of Italy. Popular for its rich culture, amazing heritage, classic history, and awe-inspiring tourist attractions, Rome is among the most visited cities among travelers. Here are some accommodation options to make your stay in Rome comfortable and within the budget. Have a look and enjoy your Rome trip"
# num="4"
# strKwds=['Eternal','of','rich', 'amazing']

mainStr="a b a d "
num=2
strKwds=["a","d","a","d"]

# mainStr=raw_input()
# num=raw_input()
# mainStr=[]
# i=0
# while(i<num):
# 	strKwds.append(raw_input())

for kwd in strKwds:
	regex=kwd.lower() + "(\s|\.)"
	if not re.search(regex,mainStr.lower()):
		print "NO SUBSEGMENT FOUND"
		exit()

def allindices(string, sub, listindex=[], offset=0):
	listindex=[]
	i = string.find(sub, offset)
	while i >= 0:
		listindex.append(i)
		i = string.find(sub, i + 1)
	return listindex

def difference(fromIndex,toIndex):
	diff = fromIndex - toIndex
	if diff == 0:
		diff=200001
	return diff

def findFromLeft(ei,kwd):
	index = mainStr.lower().find(kwd,ei)
	if index==-1:
		index=ei
	return index

def findFromRight(si,kwd):
	index= mainStr.lower().rfind(kwd,0,si)
	if index==-1:
		index=si
	return index

def searchNearestKeyword(si,ei,kwd):
	leftIndex=findFromLeft(ei,kwd)
	rightIndex=findFromRight(si,kwd)
	differenceRightIndex=difference(si,rightIndex)
	differenceLeftIndex=difference(leftIndex,ei)
	if  (differenceRightIndex < differenceLeftIndex):
		# print rightIndex,ei
		return rightIndex,ei
	else:
		if leftIndex==-1:
			pass
		# print si,mainStr.find(" ",leftIndex)
		return si,mainStr.find(" ",leftIndex)

mainList=[]
for kwd in strKwds:
	mainList.append(allindices(mainStr.lower(),kwd.lower()))
least=len(mainList[0])
shortestList=mainList[0]
for lst in mainList:
	if least > len(lst):
		least=len(lst)
		shortestList=lst

subSequenceArray=[]
for sl in shortestList:
	startIndex=sl
	endIndex=mainStr.find(" ",sl)
	# print startIndex,endIndex
	for kwd in strKwds:
		if len(kwd) in [1,2]:
			# print kwd
			kwd=kwd + " "
		regex=kwd.lower()
		if re.search(regex,mainStr[startIndex:endIndex].lower()):
			continue
		if kwd.lower() == mainStr[startIndex:endIndex].lower():
			continue
		startIndex, endIndex = searchNearestKeyword(startIndex,endIndex,kwd.lower())
	subSequenceArray.append(mainStr[startIndex:endIndex])
	minLenX = len(subSequenceArray[0])
	op = [x for x in subSequenceArray if len(x) < minLenX]
	if not op:
		op=[subSequenceArray[0]]
shortestSubSequence=re.sub(r"[^\w]"," ",op[0])     
print shortestSubSequence.replace("  "," ")