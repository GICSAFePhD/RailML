from RailML.Enumerates import LrsMethod
from RailML.Base import BaseObject,NetworkResource

class PositioningSystem(BaseObject):
    pass

class LinearPositiongSystem(PositioningSystem):
    def __init__(self) -> None:
        self.__startMeasure = "Double"
        self.__endMeasure = "Double"
        self.__linearReferencingMethod = LrsMethod.ABSOLUTE
        self.__units = "String"

    def __str__(self):
        return f'{self.__startMeasure}|{self.__endMeasure}|{self.__linearReferencingMethod}|{self.__units}'

class GeometricPositioningSystem(PositioningSystem):
    def __init__(self) -> None:
        self.__crsDefinition = "String"

    def __str__(self):
        return f'{self.__crsDefinition}'

class LinearAnchorPoint(NetworkResource):
    def __init__(self) -> None:
        self.__anchorName = "String"
        self.__measure = "Double"
        self.__measureToNext = "Double"

    def __str__(self):
        return f'{self.__anchorName}|{self.__measure}|{self.__measureToNext}'

class AssociatedPositioningSystem(NetworkResource):
    pass

class PositioningSystemCoordinate():
    pass

class LinearCoordinate(PositioningSystemCoordinate):
    def __init__(self) -> None:
        self.__lateralOffset = "Double"
        self.__verticalOffset = "Double"
        self.__measure = "Double"

    def __str__(self):
        return f'{self.__lateralOffset}|{self.__verticalOffset}|{self.__measure}'
    
class GeometricCoordinate(PositioningSystemCoordinate):
    def __init__(self) -> None:
        self.__x = "Double"
        self.__y = "Double"
        self.__z = "Double"

    def __str__(self):
        return f'{self.__x}|{self.__y}|{self.__z}'

class IntrinsicCoordinate():
    def __init__(self) -> None:
        self.__intrinsicCoord = "Double"

    def __str__(self):
        return f'{self.__intrinsicCoord}'
