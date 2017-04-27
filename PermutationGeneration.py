"""
generating random data for the permutations
class must be bigger than 5
"""
import random
import os

AMOUNT_OF_PERMUTATIONS = 100  
SIZE_OF_GROUP = 3

def modOfInput(n, sizeOfGroup):
	return (n % sizeOfGroup)

def amountOfGroups(n, sizeOfGroup):
	return (n / sizeOfGroup)

def randomData(n, sizeOfGroup):
	a = range(n)
	dataList = random.sample(a, len(a))
	counter = 0

	if modOfInput(n, sizeOfGroup) == 0:

		finalData = []
		for i in range(amountOfGroups(n, sizeOfGroup)):
			arr = [dataList[counter + j] for j in range(sizeOfGroup)]
			finalData.append(arr)
			counter += sizeOfGroup

		return finalData


	elif modOfInput(n, sizeOfGroup) != 0:
		
		amountOfExtendedGroups = modOfInput(n, sizeOfGroup)
		sizeOfExtendedGroups = sizeOfGroup + 1

		finalData = []
		for i in range(amountOfGroups(n, sizeOfGroup) - amountOfExtendedGroups):
			arr = [dataList[counter + j] for j in range(sizeOfGroup)]
			finalData.append(arr)
			counter += sizeOfGroup

		for i in range(amountOfExtendedGroups):
			arr = [dataList[counter + j] for j in range(sizeOfExtendedGroups)]
			finalData.append(arr)
			counter += sizeOfExtendedGroups

		return finalData


if __name__ == "__main__":


	os.system("mkdir Permutations/" + str(AMOUNT_OF_PERMUTATIONS) + "/")

	for classSize in range(15, 51):
		
		name = str(classSize)
		path = "./Permutations/" + str(AMOUNT_OF_PERMUTATIONS) + "/"
		fileName = path + name + ".txt"
		f = open(fileName,'w')



		for i in range(AMOUNT_OF_PERMUTATIONS):
			f.write(str(randomData(classSize, SIZE_OF_GROUP)) + "\n")

		f.close