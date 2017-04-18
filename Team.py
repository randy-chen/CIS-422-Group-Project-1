class Team:

    global Person
    Person = Person.Person()

    def __init__(self, P1, P2, P3, P4=None): #Take four or three person information to build team
        self.__goodTeam = True
        self.__memberList = [P1, P2, P3, P4]
        self.__numberofteam = len(self.__memberList)
        self.__meetList = []
        self.SORT(P1, P2, P3, P4)

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
        self.IfTimeWork()
        return None

    def IfTimeWork(self): #Check if a team could have two hour a week to meet each other
        i = 0
        work = 0
        while i < 91:
            if (self.__meetList[i] == True):
                work += 1
        if (work <= 2):
            self.__goodTeam = False
        return None

    def getSituation(self): #Return the situation if the team could work
        return self.__goodTeam

    def getTeamList(self):
        return self.__memberList

    def getNumber(self):
        return self.__numberofteam