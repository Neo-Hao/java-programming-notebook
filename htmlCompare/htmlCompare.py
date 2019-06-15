#Kira Jaeger 2019
#This program will run two  html files against eachother and check for specific differences
	#these differences include counts to check student interaction
	# and cell count to check for new data

#import beautiful soup and file
from bs4 import BeautifulSoup

#creates the Beautiful Soup
def createSoup(file):
	with open(file) as fp:
		soup = BeautifulSoup(fp, 'lxml')

	fp.close()
	return soup

#function is passed soup and pulls out how many times each code cell was run
#places "In[]" counts in to a list
#returns a list
def runArray(soup):
	inputs = []
	length = 0
	for div_tag in soup.find_all("div", class_="prompt input_prompt"):
		num = div_tag.string
		length = len(num)
		#parses out empty lines
		if num[0] == 'I':
			#og string "In [num]:"
			if length == 6:
				num = num[4:4]
			else:
				newLen = length - 6
				num = num[4:4+newLen]

			num = int(num)
			inputs.append(num)

	return inputs

#This method compares the run times and finds any differences between the original file
#	and the student's file. Returns the index position for later use
def compArrays(arOG, arComp):
	index = []
	if(len(arOG) != len(arComp)):
		index.append(400)
		return index
	else:
		for x in range (0, len(arOG)):
			if arOG[x] != arComp[x]:
				index.append(x)
		return index

#This method SHOULD return how many times the student ran a cell. Errors abound
def findRunChange(arOg, arComp, index):
	diff = []
	for x in range (0, len(index)):
		i = index[x]
		#issue here kira
		comp = arComp[i]
		og = arOG[i]
		# when you run a cell the count of the cell under it gets messed up as well....
		# better logic is needed
		if comp > og:
			num = abs(comp - og)
			diff.append(num)
	return diff

#This method will probably put the cell index and run amount into 
def twoD(index, runDiff):
	changeArr = []

	# for i in range(0, len(index)):
	# 	changeArr.append(index[i])
	# 	for j in range(0, len(runDiff)):
	# 		changeArr[i][j].append(runDiff[j])

def main():
	soupOG = createSoup("chapter1.html")
	soupCompare = createSoup("chapter1(1).html")

	ogNums = runArray(soupOG)
	compNums = runArray(soupCompare)

	changeIndex = compArrays(ogNums, compNums)

	# print(changeIndex[0])
	# print(ogNums)
	# print(compNums)
	# print(compNums[2])

	if changeIndex[0] == 400:
		#this will need a better solution
		print("Extra cells")
	elif len(changeIndex) == 0:
		print("no differences found")
	else:
		runAmount = findRunChange(soupOG, soupCompare, changeIndex)
		# runChanges = twoD(changeIndex, runAmount)

main()