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
	return str(output)


# Main Function interating for all 7 days of the week
if __name__ == "__main__":
	i = 0
	finalOutputForCSV = ""
	while i < 7:
		finalOutputForCSV += oneDayData() + ","
		i += 1
	finalOutputForCSV = finalOutputForCSV[:-1]
	print(finalOutputForCSV)