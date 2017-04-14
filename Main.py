import sys
import csv

def main():
    fileName = "aaa"
    ImportList(fileName)
    return None

    ###########################
    ### Import info from csv file. Should be passed the file name
    ### with an .csv ending. Only looks in current directory.
    ### Will look for colums with "Name" and "Email" in them
    ### to identify which columns to use. (Does not check ID, yet.)
    ### Returns a list of lists with:
    ### [[name, email, [True, False, etc],[
    def ImportList(fileName):  # fileName should end in .csv

        try:  # to load the csv file.
            with open(fileName, 'r') as f:
                reader = csv.reader(f)
                csv_list = list(reader)
        except:
            sys.exit("Unable to find the file " + fileName)

            # print (csv_list)

        weekDay = {'Sunday': 0, 'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4, 'Friday': 5, 'Saturday': 6}
        weekDict = {'Sunday': -1, 'Monday': -1, 'Tuesday': -1, 'Wednesday': -1, 'Thursday': -1, 'Friday': -1,
                    'Saturday': -1}
        listHeaders = []  # What did they name the columns in the CSV?

        # Check and Load the column names and numbers.
        for i in range(1, len(csv_list[0])):
            listHeaders.append("" + csv_list[0][i] + "")
            if "Name" in csv_list[0][i]:
                fullName = i
            if "Email" in csv_list[0][i] or "E-mail" in csv_list[0][i]:
                eMail = i
            if csv_list[0][i] == "Sunday":
                weekDict['Sunday'] = i
            if csv_list[0][i] == "Monday":
                weekDict['Monday'] = i
            if csv_list[0][i] == "Tuesday":
                weekDict['Tuesday'] = i
            if csv_list[0][i] == "Wednesday":
                weekDict['Wednesday'] = i
            if csv_list[0][i] == "Thursday":
                weekDict['Thursday'] = i
            if csv_list[0][i] == "Friday":
                weekDict['Friday'] = i
            if csv_list[0][i] == "Saturday":
                weekDict['Saturday'] = i

        firstList = []  # Full list to be returned from function.

        for i in range(1, len(csv_list)):
            availableTimes = [False] * 91
            personData = []  # list for each person.

            # Name
            personData.append("" + csv_list[i][fullName] + "")

            # ID
            personData.append("" + csv_list[i][0] + "")

            # Email
            personData.append("" + csv_list[i][eMail] + "")

            # Days of the Week
            for key, val in weekDict.items():
                if val >= 0 and csv_list[i][val] != "":
                    dayStr = "" + csv_list[i][val] + ""
                    availableTimes = TimeSplit(dayStr, availableTimes, weekDay[key])

            personData.append(availableTimes)
            # print (personData)
            firstList.append(personData)

        f.close()
        return firstList

    ##############################
    ### This function takes a string of times, (what Google gives us)
    ### splits them on the ; and turns them into a True or False
    ### in the availableTimes list.
    ### It is assumed that there are only 13 time slots a day.
    ### AKA dayOffset.
    ### It is assumed that the earliest time available is 8am
    ### AKA startOfDay
    def TimeSplit(dayString, availableTimes, dayOffset):
        dayOffset = 13 * dayOffset
        startOfDay = 8
        endOfDay = startOfDay + 13

        availTimeList = dayString.split(';')
        for i in availTimeList:
            if (i[0] == "1") and (i[1] != "a") and (i[1] != "p"):
                dayTime = "" + i[0] + i[1] + ""
                dayAmPm = i[2]
            else:
                dayTime = "" + i[0] + ""
                dayAmPm = i[1]
            if dayAmPm == "p":
                dayInt = int(dayTime) + 12
            else:
                dayInt = int(dayTime)

            if dayInt > startOfDay and dayInt < endOfDay:
                dayTrue = dayInt - startOfDay + dayOffset

                availableTimes[dayTrue] = True

        return availableTimes
