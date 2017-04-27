"""
randDataGen.py
Author: 
    Theodore J. LaGrow
Language: Python 3.5x
Packages needed: random, randint

"""

import random
from random import randint 

# Function to generate random times for a single day
def oneDayData():
	timeData = ['8am', '9am', '10am', '11am', '12pm', '1pm', '2pm', '3pm', '4pm', '5pm', '6pm', '7pm', '8pm']
	randAmount = randint(0, len(timeData))

	outputList = []
	i=0
	while i < randAmount:
		choice = random.choice(timeData)
		if choice not in outputList:
			outputList.append(choice)
		i += 1

	output = ""
	for i in outputList:
		output += i+";"
	output = output[:-1]
	return output

# Format the string for the 7 days
def finalCSV():
	i = 0
	finalOutputForCSV = ""
	while i < 7:
		finalOutputForCSV += oneDayData() + ","
		i += 1
	finalOutputForCSV = finalOutputForCSV[:-1]
	return finalOutputForCSV


# Main Function interating for all 7 days of the week
if __name__ == "__main__":
	
	# Clearing the contents of output.txt
	open('output.txt', 'w').close()

	i=0
	while i < 40:
		with open("text.txt", "a") as f:
			f.write(finalCSV() + "\n")
		i += 1
		