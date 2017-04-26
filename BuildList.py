class buildlist:

    global Person
    Person = Person.Person()
    global Grade
    Grade = Grade.Grade()
    global Caculate
    Caculate = Caculate.Caculate()

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

    def Final(self):
        return self.__Final