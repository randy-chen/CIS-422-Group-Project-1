class Grade:

    global Person
    Person = Person.Person()

    def __init__(self, PersonList): #Take four or three person information to build team
        self.__memberList = PersonList
        self.__numberofteam = len(self.__memberList)
        self.__meetList = []
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
                i += 1
            else:
                ML.append(False)
                i += 1
        self.__meetList = ML
        self.CaculateTimeGrade()
        return None

    def getTeamList(self):
        return self.__memberList

    def getNumber(self):
        return self.__numberofteam

    def CaculateTimeGrade(self):
        T = 0
        for time in self.__meetList:
            if (time == True):
                T += 1
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