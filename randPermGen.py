"""
generating random data for the permutations
class must be bigger than 5
"""
import random
import os

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

	amountOfPermutations = 100000  # Change value for the amount of permutations
	sizeOfGroup = 3
	os.system("mkdir Permutations" + str(amountOfPermutations) + "/")

	for classSize in range(15, 51):
		
		name = "size" + str(classSize) + "Perm" + str(amountOfPermutations)
		path = "./Permutations" + str(amountOfPermutations) + "/"
		fileName = path + name + ".txt"
		f = open(fileName,'w')



		for i in range(amountOfPermutations):
			f.write(str(randomData(classSize, sizeOfGroup)) + "\n")

		f.close