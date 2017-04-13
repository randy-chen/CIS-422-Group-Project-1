class Person:

    NumberOfPerson = 0;

    def __init__(self, name, id, email, datelist):
        self.__name = name
        self.__id = id
        self.__email = email
        self.__datelist = datelist

    def getName(self):
        return self.__name

    def getID(self):
        return self.__id

    def getEmail(self):
        return self.__email

    def getDateList(self):
        return self.__datelist

    def setName(self, name):
        self.__name = name
        return None

    def setID(self, id):
        self.__id = id

    def setEmail(self, email):
        self.__email = email
        return None

    def setDateList(self, datelist):
        self.__datelist = datelist
        return None