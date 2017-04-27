#!/usr/bin/env python3
# Main.py

import sys
import csv
import ast



def Start():
    """
    Start() runs the full stack of the algorithm.  
    Takes in a csv and exports a csv in the correct location for React.
    """

    dirpath = os.path.dirname(os.path.abspath(__file__))
    inputfile = '../Front_End/storage/input.csv'
    outputfile = '../Front_End/storage/output.csv'
    inputfilepath = os.path.join(dirpath, inputfile)
    outputfilepath = os.path.join(dirpath, outputfile)
    with open(inputfilepath,'r') as csvinput:
        with open(outputfilepath, "w") as csvoutput:

            # writing to the output csv
            writer = csv.writer(csvoutput, lineterminator='\n')
            reader = csv.reader(csvinput)
            csv_list = list(reader)
            all = []

            row = csv_list[0]
            cList = iter(csv_list)

            row.append("Assigned Team")
            row.append("Assigned Team 2")
            row.append("Assigned Team 2")
            all.append(row)
            next(cList)

           
            # running the program
            deal = Deal()
            Input = deal.ImportList(file)
            bl = Buildlist(Input)
            OutPut = bl.Final()
            
            M = 0
            finalTeams0 = {}
            finalTeams1 = {}
            finalTeams2 = {}
            for Model in OutPut:
                """
                # uncomment for testing
                print("Model ", M) 
                print("Model Grade ", Model.GetGrade()) #Getting the overal score
                """
                TeamList = Model.GetTeamList()
                T = 0
                for Team in TeamList:
                    T += 1
                    """
                    # uncomment for testing
                    print("Team", T)
                    print("Team score ", Team.GetMeetingTime())
                    """             
                    PersonList = Team.getPersonList()
                    for Person in PersonList:
                        """
                        # uncomment for testing
                        print(Person.getName())
                        """
                        if M == 0:
                            finalTeams0[Person.getName()] = T
                        elif M == 1:
                            finalTeams1[Person.getName()] = T
                        elif M == 2:
                            finalTeams2[Person.getName()] = T

                """
                # uncomment for testing
                print()
                avgTeamMeetingTime = float(teamCounter/Model.GetNumberOfTeams())
                print(avgTeamMeetingTime)
                print()
                print("Model {0}: \n {1}".format(M, finalTeams))
                """
                M += 1

            # adding the top 3 teams to the columns
            for row in cList:
                row.append(finalTeams0[row[1]])
                row.append(finalTeams1[row[1]])
                row.append(finalTeams2[row[1]])
                all.append(row)

            writer.writerows(all)
        csvoutput.close()
    
    csvinput.close()

    return None



class Deal:
    """
    Import info from csv file. Should be passed the file name
    with an .csv ending. Only looks in current directory.
    Will look for colums with "Name" and "Email" in them
    to identify which columns to use. (Does not check ID, yet.)
    Returns a list of lists with:
    [[name, email, [True, False, etc],[
    """
    def ImportList(self, fileName): 
        """
        This function takes a string of times, (what Google gives us)
        splits them on the ; and turns them into a True or False
        in the availableTimes list.
        It is assumed that there are only 13 time slots a day.
        AKA dayOffset.
        It is assumed that the earliest time available is 8am
        AKA startOfDay
        """

        try:  # to load the csv file.
            with open(fileName, 'r') as f:
                reader = csv.reader(f)
                csv_list = list(reader)
        except:
            sys.exit("Unable to find the file " + fileName)
            # print (csv_list) #uncomment for testing

        weekDay = {'Sunday': 0, 'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4, 'Friday': 5, 'Saturday': 6}
        weekDict = {'Sunday': -1, 'Monday': -1, 'Tuesday': -1, 'Wednesday': -1, 'Thursday': -1, 'Friday': -1,
                    'Saturday': -1}
        listHeaders = []  # What did the input file name the columns in the CSV
        fullName = None
        IDnumber = None
        eMail = None

        # Check and Load the column names and numbers.
        for i in range(1, len(csv_list[0])):
            listHeaders.append("" + csv_list[0][i] + "")
            if "Name" in csv_list[0][i]:
                fullName = i
            if "ID" in csv_list[0][i] or "id" in csv_list[0][i]:
                IDnumber = i
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
                    availableTimes = self.TimeSplit(dayStr, availableTimes, weekDay[key])

            personData.append(availableTimes)
            firstList.append(personData)

        f.close()
        return firstList

    def TimeSplit(self, dayString, availableTimes, dayOffset):
        """
        TimeSplit() sets the times of each person in the 3D data structure
        """
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

class Buildlist:
    """
    
    """
    def __init__(self, Input):
        """

        standard initialization for Buildlist class
        Input = [[name, ide, email, [True, False, False]],......]
        """
        self.__PersonList = []
        self.__NoP = 0
        self.__Final = [] #Final output
        self.BuildPersonList(Input)

    def GetNoP(self):
        """
        GetNoP() returns the number of people in the list
        """
        return self.__NoP

    def BuildPersonList(self, input):
        """
        Build person list by Input and decide number of four and three person team
        """
        while len(input) != 0:
            person = input.pop(0)
            name = person.pop(0)
            id = person.pop(0)
            email = person.pop(0)
            time = person.pop(0)
            self.__PersonList.append(Person(name, id, email, time))
            self.__NoP += 1
        self.Creat()
        return None

    def Creat(self):
        """
        
        """
        filename = "./Permutations/10000/" + str(self.__NoP) + ".txt"
        f = open(filename, 'r')
        for Line in f:
            Line = ast.literal_eval(Line)
            TeamList = []
            for Part in Line:
                PersonList = []
                for index in Part:
                    PersonList.append(self.__PersonList[index])
                team = Team(PersonList)
                TeamList.append(team)
            model = Model(TeamList)
            self.GetFinal(model)
        return None

    def GetFinal(self, Permunatetion):
        """
        GetFinal() will take the given permutation rank each perm
        and keep the top three
        """
        if(self.__Final == []):
            self.__Final.append(Permunatetion)
        else:
            x = len(self.__Final)
            for x in self.__Final:
                if(Permunatetion.GetGrade() >= x.GetGrade()):
                    i = self.__Final.index(x)
                    self.__Final.insert(i, Permunatetion)
                    break
        if (len(self.__Final) > 3):
            self.__Final = self.__Final[:3]
        return None

    def Final(self):
        """
        returns the final permutations
        """
        return self.__Final

class Model:
    def __init__(self, TeamList):
        """
        standard initialization for Model class
        """
        self.__TeamList = TeamList
        self.__NumberOfTeams = len(self.__TeamList)
        self.__Grade = 0
        self.CG()

    def CG(self):
        for team in self.__TeamList:
            self.__Grade += team.GetGrade()

    def GetTeamList(self):
        """
        returns the lists on the team
        """
        return self.__TeamList

    def GetGrade(self):
        """
        returns the permutations weighted score
        """
        return self.__Grade

    def GetNumberOfTeams(self):
        """
        returns the number of teams in the Model
        """
        return self.__NumberOfTeams


class Team:
    """

    """
    def __init__(self, PersonList): 
        """
        standard initialization for Team class
        takes four or three person information to build team
        """
        self.__memberList = PersonList
        self.__numberofteam = len(self.__memberList)
        self.__meetList = []
        self.__meetingtime = 0
        self.__Grade = -1000
        self.Devid()

    def GetMeetingTime(self):
        return self.__meetingtime

    def Devid(self):
        if (self.__memberList == 4):
            p1 = self.__memberList[0]
            p2 = self.__memberList[1]
            p3 = self.__memberList[2]
            p4 = self.__memberList[3]
            self.SORT4(p1, p2, p3, p4)
        else:
            p1 = self.__memberList[0]
            p2 = self.__memberList[1]
            p3 = self.__memberList[2]
            self.SORT3(p1, p2, p3)

    def SORT3(self, p1, p2, p3): #Build the List of time which is worked for everyone in team
        ML = []
        i = 0
        l1 = p1.getDateList()
        l2 = p2.getDateList()
        l3 = p3.getDateList()
        while i < 91:
            if l1[i] == l2[i] == l3[i] == True:
                ML.append(True)
            else:
                ML.append(False)
                self.__meetingtime += 1
            i += 1
        self.__meetList = ML
        self.CaculateTimeGrade()
        return None

    def SORT4(self, p1, p2, p3, p4=None): #Build the List of time which is worked for everyone in team
        ML = []
        i = 0
        l1 = p1.getDateList()
        l2 = p2.getDateList()
        l3 = p3.getDateList()
        l4 = p4.getDateList()
        while i < 91:
            if l1[i] == l2[i] == l3[i] == l4[i] == True:
                ML.append(True)
            else:
                ML.append(False)
                self.__meetingtime += 1
            i += 1
        self.__meetList = ML
        self.CaculateTimeGrade()
        return None

    def getPersonList(self):
        return self.__memberList

    def CaculateTimeGrade(self):
        T = self.__meetingtime
        if(T>0):
            self.__Grade = 0
            if(T<4):
                self.__Grade = T*10
            elif(T<8):
                self.__Grade = 40 + (T-4)*5
            else:
                self.__Grade = 60 + (T-8)
            return  None
        else:
            return None

    def GetGrade(self):
        return self.__Grade

class Person:
    """
    The Person class holds the information and structure for
    the row in the csv.  Included is:
        name of the person
        id for the person
        email of the person
        datas stored in the datalist for the perosn
    """
    def __init__(self, name, id, email, datelist):
        """
        standard initialization for Person class
        """
        self.__name = name
        self.__id = id
        self.__email = email
        self.__datelist = datelist

    def getName(self):
        """
        Return the name of person
        """
        return self.__name

    def getID(self):
        """
        Return the ID of person
        """
        return self.__id

    def getEmail(self):
        """
        Return the email of person
        """
        return self.__email

    def getDateList(self):
        """
        Return the availbale time list of person
        """
        return self.__datelist


if __name__ == "__main__":
    """
    Initialize Program
    """
    Start() 
