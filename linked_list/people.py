class People:
    def __init__(self, name, value, next):
        self.__name = name
        self.__value = value
        self.__next = next

    @property
    def value(self):
        return self.__value

    @property
    def name(self):
        return self.__value

    @property
    def next(self):
        return self.__value

    @next.setter
    def next(self, next):
        self.__next = next
