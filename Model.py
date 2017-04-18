class Model:

    global Team
    Team = Team.Team()

    def __init__(self, NoT, NoF, PersonList):
        self.__TeamList = []
        self.__NumberOfThreePersonTeam = NoT
        self.__NumberOfFourPersonTeam = NoF
        self.__goodModel = True
        self.DevideIntoTeam(PersonList)

    def DevideIntoTeam(self, PersonList): #Build team list
        t = self.__NumberOfThreePersonTeam
        f = self.__NumberOfFourPersonTeam
        while t != 0: #Build three person team
            p1 = PersonList.pop()
            p2 = PersonList.pop()
            p3 = PersonList.pop()
            self.__TeamList.append(Team(p1, p2, p3))
            t -= 1
        while f != 0: #Build four person team
            p1 = PersonList.pop()
            p2 = PersonList.pop()
            p3 = PersonList.pop()
            p4 = PersonList.pop()
            self.__TeamList.append(Team(p1, p2, p3, p4))
            f -= 1
        self.IfGoodModel()
        return None

    def IfGoodModel(self): #Check every team in model to see if all of them is worked team
        for team in self.__TeamList:
            if (team.getSituation() == False):
                self.__goodModel = False
        return None

    def GetModelSituation(self):
        return self.__goodModel

    def GetTeamList(self):
        return self.__TeamList