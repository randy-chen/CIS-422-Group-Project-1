import itertools

class BuildList:

    global Person
    Person = Person.Person()
    global Team
    Team = Team.Team()
    global Model
    Model = Model.Model()

    def __init__(self, Input):
        self.__workedModelList = []
        self.__PersonList = []
        self.__UnSameWorkedList = []
        self.__NoT = 0
        self.__NoF = 0
        self.BuildPersonList(Input)

    def BuildPersonList(self, input):
        while len(input) != 0:
            person = input.pop
            name = person.pop
            id = person.pop
            email = person.pop
            time = person.pop
            self.__PersonList.append(Person(name, id, email, time))
            Person.NumberOfPerson += 1
        n = Person.NumberOfPerson
        self.__NoF = n%3
        self.__NoT = n/3 - n%3
        self.Creat()
        return None

    def Creat(self):
        ListofPerson = self.__PersonList
        AllKinds = itertools.permutations(ListofPerson)
        for kind in AllKinds:
            self.BuildModel(kind)


        self.Reform()
        self.__UnSameWorkedList.append(self.__workedModelList[0])
        for workedmodel in self.__workedModelList:
            for model in self.__UnSameWorkedList:
                if(self.CheckSameModel(workedmodel, model) == False):
                    self.__UnSameWorkedList.append(workedmodel)
        return None

    def BuildModel(self, PersonList):
        model = Model(self.__NoT, self.__NoF, PersonList)
        if(model.GetModelSituation() == True):
            self.__workedModelList.append(model)
        return None

    def CheckSameModel(self, workedmodel, sourcemodel):
        workedteamlist = workedmodel.GetTeamList()
        sourceteamlist = sourcemodel.GetTeamList()
        sameteam = 0
        for workedteam in workedteamlist:
            for sourceteam in sourceteamlist:
                if(self.CheckSameTeam(workedteam, sourceteam) == True):
                    sameteam += 1
        if (sameteam == self.__NoT + self.__NoF):
            return True
        return False

    def CheckSameTeam(self, TeamA, TeamB):
        if(TeamA.getNumber() == TeamB.getNumber()):
            return False
        sameperson = 0
        for personA in TeamA:
            for personB in TeamB:
                if (personA.getID() == personB.getID()):
                    sameperson += 1
        if(sameperson == TeamA.getNumber()):
            return True
        return False
        
    def Reform(self):
        if (self.__workedModelList == []):
            self.__NoT = self.__NoT - 4
            self.__NoF = self.__NoF + 3
            self.Creat()
        return None