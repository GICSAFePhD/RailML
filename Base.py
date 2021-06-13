
class BaseObject():
    def __init__(self) -> None:
        self.__id = "UUID"
        self.__name = "String"
        self.__validTo = "Date"
        self.__validFrom = "Date"

    def __str__(self):
        return f'{self.__id}|{self.__name}|{self.__validTo}|{self.__validFrom}'

class NetworkResource(BaseObject):
    pass

class Network(BaseObject):
    pass

class LevelNetwork(BaseObject):
    pass
