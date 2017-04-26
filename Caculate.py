class Caculate:

    global Grade
    Grade = Grade.Grade()

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