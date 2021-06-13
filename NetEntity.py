from RailML.Base import NetworkResource
from RailML.Enumerates import ApplicationDirection

class NetEntity(NetworkResource):
    pass

class LocatedNetEntity(NetEntity):
    pass

class EntityLocation(NetworkResource):
    pass

class AreaLocation(EntityLocation):
    pass

class LinearLocation(EntityLocation):
    def __init__(self) -> None:
        self.__applicationDirection = ApplicationDirection.NORMAL

    def __str__(self):
        return f'{self.__applicationDirection}'

class LinearLocationCoordinate(LinearLocation):
    def __init__(self) -> None:
        self.__applicationDirection = ApplicationDirection.NORMAL

    def __str__(self):
        return f'{self.__applicationDirection}'
    
class SpotLocation(EntityLocation):
    def __init__(self) -> None:
        self.__applicationDirection = ApplicationDirection.NORMAL

    def __str__(self):
        return f'{self.__applicationDirection}'

class AreaLocationCoordinate(LinearLocation):
    pass

class SpotLocationIntrinsic(SpotLocation):
    def __init__(self) -> None:
        self.__applicationDirection = ApplicationDirection.NORMAL

    def __str__(self):
        return f'{self.__applicationDirection}'
    
class SpotLocationCoordinate(SpotLocation):
    pass

class StructureNetEntity(NetEntity):
    pass

class SignallingNetEntity(NetEntity):
    pass

class DressingNetEntity(NetEntity):
    pass

class Tunnel(NetEntity):
    pass

class InterlockingNetEntity(NetEntity):
    pass

class LevelCrossing(NetEntity):
    pass

class SpeedLimit(NetEntity):
    pass