import sys
import csv

def Start():
    main = Main()
    fileName = 'Test_Data_For_422_Small.csv' #need to hardcode the path from react
    Input = main.ImportList(fileName)
    OutPut = Buildlist(Input)
    return None

class Main:
    ###########################
    ### Import info from csv file. Should be passed the file name
    ### with an .csv ending. Only looks in current directory.
    ### Will look for colums with "Name" and "Email" in them
    ### to identify which columns to use. (Does not check ID, yet.)
    ### Returns a list of lists with:
    ### [[name, email, [True, False, etc],[
    def ImportList(self, fileName):  # fileName should end in .csv

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
    def TimeSplit(self, dayString, availableTimes, dayOffset):
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

    def __init__(self, Input): #Input = [[name, ide, email, [True, False, False]],......]
        self.__PersonList = []
        self.__Final = [] #Final output
        self.BuildPersonList(Input)
        self.Final()

    def BuildPersonList(self, input): #Build person list by Input and decide number of four and three person team
        while len(input) != 0:
            person = input.pop(0)
            name = person.pop(0)
            id = person.pop(0)
            email = person.pop(0)
            time = person.pop(0)
            self.__PersonList.append(Person(name, id, email, time))
            Person.NumberOfPerson += 1
        self.Creat()
        return None

    def Creat(self):
        filename = "./Permutations/10000/" + str(Person.NumberOfPerson) + ".txt"
        f = open(filename, 'r')
        for Line in f:
            TeamList = []
            for Part in Line:
                PersonList = []
                for index in Part:
                    PersonList.append(self.__PersonList[int(index)])
                Team = Grade(PersonList)
                TeamList.append(Team)
            Model = Caculate(TeamList)
            self.GetFinal(Model)
        return None

    def GetFinal(self, Permunatetion):
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
            self.__Final.pop()
        return None

    def Final(self):
        return self.__Final

class Grade:

    def __init__(self, PersonList): #Take four or three person information to build team
        self.__memberList = PersonList
        self.__numberofteam = len(self.__memberList)
        self.__meetList = []
        self.__meetingtime = 0
        self.__Grade = -1000
        self.CaculateTimeGrade()

    def Devid(self, List):
        if (self.__memberList == 4):
            p1 = self.__memberList[0]
            p2 = self.__memberList[1]
            p3 = self.__memberList[2]
            p4 = self.__memberList[3]
            self.SORT(p1, p2, p3, p4)
        else:
            p1 = self.__memberList[0]
            p2 = self.__memberList[1]
            p3 = self.__memberList[2]
            self.SORT(p1, p2, p3)


    def SORT(self, p1, p2, p3, p4=None): #Build the List of time which is worked for everyone in team
        ML = []
        i = 0
        while i < 91:
            if p1[i] == p2[i] == p3[i] == p4[i] == True:
                ML.append(True)
            else:
                ML.append(False)
                self.__meetingtime += 1
            i += 1
        self.__meetList = ML
        self.CaculateTimeGrade()
        return None

    def getTeamList(self):
        return self.__memberList

    def getNumber(self):
        return self.__numberofteam

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

class Caculate:

    def __init__(self, GradeList):
        self.__TeamList = GradeList
        self.__Grade = 0
        self.CG()

    def CG(self):
        for team in self.__TeamList:
            self.__Grade += team.GetGrade()

    def GetGradeList(self):
        return self.__TeamList

    def GetGrade(self):
        return self.__Grade

class Person:

    NumberOfPerson = 0

    def __init__(self, name, id, email, datelist):
        self.__name = name
        self.__id = id
        self.__email = email
        self.__datelist = datelist

    def getName(self): #Return the name of person
        return self.__name

    def getID(self): #Return the ID of person
        return self.__id

    def getEmail(self): #Return the email of person
        return self.__email

    def getDateList(self): #Return the availbale time list of person
        return self.__datelist

    def setName(self, name):
        self.__name = name
        return None

    def setID(self, id):
        self.__id = id

    def setEmail(self, email):
        self.__email = email
        return None

    def setDateList(self, datelist):
        self.__datelist = datelist
        return None

Start()