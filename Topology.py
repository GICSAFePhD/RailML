from RailML.Base import NetworkResource
from RailML.Enumerates import Navigability, Usage

class NetElement(NetworkResource):
    pass

class Relation(NetworkResource):
   pass
    
class PositionedRelation(Relation):
    def __init__(self) -> None:
        self.__navigability = Navigability.NONE
        self.__positionOnA = Usage.USING_START
        self.__positionOnB = Usage.USING_START

    def __str__(self):
        return f'{self.__navigability}|{self.__positionOnA}|{self.__positionOnB}'

class CompositionNetElt(NetElement):
    pass

class ElementPartCollection():
    pass

class PositioningNetElement(CompositionNetElt):
    pass

class LinearElement(PositioningNetElement):
    pass

class NonLinearElement(PositioningNetElement):
    pass

class AssociatedNetElement():
    def __init__(self) -> None:
        self.__intrinsicCoordBegin = "Double"
        self.__intrinsicCoordEnd = "Double"
        self.__keepsOrientation = "Bool"

    def __str__(self):
        return f'{self.__intrinsicCoordBegin}|{self.__intrinsicCoordEnd}|{self.__keepsOrientation}'
    
class OrderedAssociatedNetElement(AssociatedNetElement):
    def __init__(self) -> None:
        self.__sequence = "Int"

    def __str__(self):
        return f'{self.__sequence}'
    
class OrderedCollection(ElementPartCollection):
    def __init__(self) -> None:
        self.__sequence = "Int"

    def __str__(self):
        return f'{self.__sequence}'

class UnorderedCollection(ElementPartCollection):
    pass

class Trail(LinearElement):
    pass

class SectionOfLine(LinearElement):
    pass

class NetLimit(NonLinearElement):
    pass

class OperationalPoint(NonLinearElement):
    pass