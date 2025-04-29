from Task import Task

class Manager:
    def __init__(self):
        self.__tasks = []
        self.__used_ids = []
        self.__id = 0
        
    def createTask(self, author, text):
        if self.__id not in self.__used_ids:
            task = Task(author, text, self.__id)
        else:
            return Exception
        self.__tasks.append(task)
        self.__used_ids.append(self.__id)
        self.__id += 1

    def deleteTask(self, id):
        for i in self.__tasks:
            if i.getID() == id:
                self.__tasks.remove(i)
                self.__used_ids.remove(id)

    def GetTasks(self):
        return self.__tasks

    