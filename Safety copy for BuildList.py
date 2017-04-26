import itertools

class BuildList:

    global Person
    Person = Person.Person()
    global Team
    Team = Team.Team()
    global Model
    Model = Model.Model()
    global Grade
    Grade = Grade.Grade()
    global Caculate
    Caculate = Caculate.Caculate()

    def __init__(self, Input): #Input = [[name, ide, email, [True, False, False]],......]
        self.__PersonList = []
        self.BuildPersonList(Input)
        self.__Final = [] #Final output
        #self.__workedModelList = []
        #self.__UnSameWorkedList = []
        #self.__NoT = 0
        #self.__NoF = 0

    def BuildPersonList(self, input): #Build person list by Input and decide number of four and three person team
        while len(input) != 0:
            person = input.pop(0)
            name = person.pop(0)
            id = person.pop(0)
            email = person.pop(0)
            time = person.pop(0)
            self.__PersonList.append(Person(name, id, email, time))
            Person.NumberOfPerson += 1
        n = Person.NumberOfPerson
        self.__NoF = n%3
        self.__NoT = n/3 - n%3
        self.Creat()
        return None

    def Creat(self):
        filename = "./Permutations/10000/" + Person.NumberOfPerson
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





    def another(self):
        AllKinds = itertools.permutations(self.__PersonList) #Get all permunatation of person list
        for kind in AllKinds:
            self.BuildModel(kind)
        self.Reform()
        for workedmodel in self.__workedModelList:
            for model in self.__UnSameWorkedList:
                if(self.CheckSameModel(workedmodel, model) == False):
                    self.__UnSameWorkedList.append(workedmodel)
        self.__Final = self.__UnSameWorkedList[0]
        for model in self.__UnSameWorkedList:
            if(model.GetGrade() > self.__Final.GetGrade()):
                self.__Final = model
        return None

    def BuildModel(self, PersonList): #Build Model
        model = Model(self.__NoT, self.__NoF, PersonList)
        if(model.GetModelSituation() == True): #Check if model work
            self.__workedModelList.append(model)
        return None

    def CheckSameModel(self, workedmodel, sourcemodel): #Check if two model are same
        numberofteam = self.__NoF + self.__NoT
        workedteamlist = workedmodel.GetTeamList()
        sourceteamlist = sourcemodel.GetTeamList()
        sameteam = 0
        for team in workedteamlist:
            for goodteam in sourceteamlist:
                if(self.CheckSameTeam(team, goodteam) == True):
                    sameteam += 1
        if (sameteam == numberofteam):
            return True
        return False

    def CheckSameTeam(self, TeamA, TeamB): #Check if two team has same person by check their ID.
        if(TeamA.getNumber() != TeamB.getNumber()):
            return False
        sameperson = 0
        for personA in TeamA:
            for personB in TeamB:
                if (personA.getID() == personB.getID()):
                    sameperson += 1
        if(sameperson == TeamA.getNumber()):
            return True
        return False
        
    def Reform(self): #Remfor the number of three person team and four person team
        if (self.__workedModelList == []):
            self.__NoT = self.__NoT - 4
            self.__NoF = self.__NoF + 3
            if(self.__NoT >= 0):
                self.Creat()
            else:
                self.__Final = "None worked Model"
        return None