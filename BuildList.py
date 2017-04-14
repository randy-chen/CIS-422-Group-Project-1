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
        n = len(self.__PersonList)
        self.__NoF = n%3
        self.__NoT = n/3 - n%3
        return None

    def Creat(self):
        ListofPerson = self.__PersonList


        AllKinds = []
        for kind in AllKinds:
            self.BuildModel(kind)
        NewList = []
        NewList.append(self.__workedModelList[0])
        for workedmodel in self.__workedModelList:
            for model in NewList:
                if(self.CheckSameModel(workedmodel, model) == False):
                    NewList.append(workedmodel)
        self.__UnSameWorkedList = NewList
        return None

    def BuildModel(self, PersonList):
        model = Model(self.__NoT, self.__NoF, PersonList)
        if(model.GetModelSituation() == True):
            self.__workedModelList.append(model)
        return None

    def CheckSameModel(self, ModelA, ModelB):
        MAT = ModelA.GetTeamList()
        MBT = ModelB.GetTeamList()
        for AT in MAT:
            for BT in MBT:
                if(self.CheckSameTeam(AT, BT, True) == False):
                    return False
        return True

    def CheckSameTeam(self, TeamA, TeamB, flag):
        if(TeamA.getNumber() != TeamB.getNumber()):
            flag = False
        else:
            sameperson = 0
            for pa in TeamA:
                for pb in TeamB:
                    if(pa.getName() == pb.getName()):
                        sameperson += 1
            if(sameperson == TeamA.getNumber()):
                flag = False
        return flag