class Task:
    def __init__(self, author, task, iid):
        self.__author = author
        self.__task = task
        self.__id = iid

    def getAuthor(self):
        return self.__author
    
    def getTask(self):
        return self.__task
    
    def setAuthor(self, author):
        self.__author = author
    
    def setTask(self, task):
        self.__task = task

    def setID(self, id):
        self.__id = id

    def getID(self):
        return self.__id

    def __str__(self):
        return f'author: {self.__author}, task: {self.__task}'