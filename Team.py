class Team:

    global Person
    Person = Person.Person()

    def __init__(self, P1, P2, P3, P4=None):
        self.__memberList = [P1, P2, P3, P4]
        self.__numberofteam = len(self.__memberList)
        self.__meetList = []
        self.MeetTimeList()

    def MeetTimeList(self):
        ML = []
        p1 = self.__memberList[0]
        p2 = self.__memberList[1]
        p3 = self.__memberList[2]
        if (self.__numberofteam == 4):
            p4 = self.__memberList[3]
        if (self.__numberofteam == 3):
            self.Mfor3(p1, p2, p3)
        else:
            self.Mfor4(p1,p2,p3,p4)
        return None

    def Mfor3(self, p1, p2, p3):
        ML = []
        l1 = p1.getDateList()
        l2 = p2.getDateList()
        l3 = p3.getDateList()
        i = 0
        while i < 91:
            if l1[i] == l2[i] == l3[i] == True:
                ML.append(True)
                i += 1
            else:
                ML.append(False)
        return None

    def Mfor4(self, p1, p2, p3, p4):
        ML = []
        l1 = p1.getDateList()
        l2 = p2.getDateList()
        l3 = p3.getDateList()
        l4 = p3.getDateList()
        i = 0
        while i < 91:
            if l1[i] == l2[i] == l3[i] == l4[i] == True:
                ML.append(True)
                i += 1
            else:
                ML.append(False)
        return None

    def IfTimeWork(self):
        i = 0
        work = 0
        while i < 91:
            if (self.__meetList[i] == True):
                work += 1
        if (work >= 2):
            return True
        else:
            return False