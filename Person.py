class Person:

    NumberOfPerson = 0

    def __init__(self, name, id, email, datelist):
        self.__name = name
        self.__id = id
        self.__email = email
        self.__datelist = datelist

    def getName(self): #Return the name of person
        return self.__name

    def getID(self): #Return the ID of person
        return self.__id

    def getEmail(self): #Return the email of person
        return self.__email

    def getDateList(self): #Return the availbale time list of person
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