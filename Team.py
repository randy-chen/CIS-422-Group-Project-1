class Team:

    global Person
    Person = Person.Person()

    def __init__(self, P1, P2, P3, P4=None):
        self.__goodTeam = True
        self.__memberList = [P1, P2, P3, P4]
        self.__numberofteam = len(self.__memberList)
        self.__meetList = []
        self.SORT(P1, P2, P3, P4)

    def SORT(self, p1, p2, p3, p4 = None):
        ML = []
        i = 0
        while i < 91:
            if p1[i] == p2[i] == p3[i] == p4[i] == True:
                ML.append(True)
                i += 1
            else:
                ML.append(False)
        self.IfTimeWork()
        return None

    def IfTimeWork(self):
        i = 0
        work = 0
        while i < 91:
            if (self.__meetList[i] == True):
                work += 1
        if (work <= 2):
            self.__goodTeam = False
        return None

    def getSituation(self):
        return self.__goodTeam

    def getTeamList(self):
        return self.__memberList

    def getNumber(self):
        return self.__numberofteam