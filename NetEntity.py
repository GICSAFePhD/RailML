from RailML.Base import NetworkResource
from RailML.Enumerates import ApplicationDirection

class NetEntity(NetworkResource):
    """ 
    !Defines the generic parent class for all the information that can be associated 
    ! with the network considered. Information may be, for instance: tunnels, signals,
    ! level crossings, track circuits, speed limites, etc.
    *Derivates from: 
        NetworkResource    
    """
    pass

class LocatedNetEntity(NetEntity):
    """ 
    !Defines a parent class for information that can definitely be localizad, which
    ! is the case of the most infrastructure-related objects.
    *Derivates from: 
        NetEntity    
    *Composition: 
        1...* EntityLocation
    *Remove: (!) 
        Whenever a LocatedNetEntity instance is removed, all related EntityLocation could continue to exist.       
    """

class EntityLocation(NetworkResource):
    """ 
    !Defines topological and positional location information for NetEntity instances.
    *Derivates from: 
        NetworkResource    
    *Belongs to: 
        1 LocatedNetEntity
    """
        
class SpotLocation(EntityLocation):
    """ 
    !Defines point location information for LocatedNetEntity instances in reference
    ! to one PosioningNetElement instance.
    *Derivates from: 
        EntityLocation   
    *Parameters
    ----------
    applicationDirection:-> ApplicationDirection
        normal: the located object is valid in the direction of the LinearElement.
        reverse: the located object is valid in the reverse direction of the LinearElement.
        both: the located object is valid in both directions.
    ---------   
    *Has: 
        * PositioningNetElement   
    """
    #def __init__(self) -> None:
    #    self.__applicationDirection = ApplicationDirection.NORMAL

    #def __str__(self):
    #    return f'{self.__applicationDirection}'

class SpotLocationIntrinsic(SpotLocation):
    """
    !Defines additional information in respect of intrinsic positioning for a
    ! SportLocation instance
    *Derivates from: 
        SpotLocation   
    *Parameters
    ----------
    intrinsicCoord: -> Double
        Location in reference to the chosen NetElement given as value in the interval from 0 to 1.
    ---------   
    """
    #def __init__(self) -> None:
    #    self.__applicationDirection = ApplicationDirection.NORMAL

    #def __str__(self):
    #    return f'{self.__applicationDirection}'
    
class SpotLocationCoordinate(SpotLocation):
    """
    !Defines the relation between a SportLocation and PositioningSystemCoordinate.
    *Derivates from: 
        SpotLocation   
    *Parameters
    ----------
    applicationDirection:-> ApplicationDirection
        normal: the located object is valid in the direction of the LinearElement.
        reverse: the located object is valid in the reverse direction of the LinearElement.
        both: the located object is valid in both directions.
    ---------
    *Has:
        1 PositioningSystemCoordinates   
    """    
    pass 

class LinearLocation(EntityLocation):
    """
    !Defines location information with a startpoint and an endpoint for LocatedNetEntity
    ! instances in reference to one or more PositioningNetElement instances. The set of
    ! associated PositioningNetElement instances is ordered.
    *Derivates from: 
        EntityLocation   
    *Parameters
    ----------
    applicationDirection:-> ApplicationDirection
        normal: the located object is valid in the direction of the LinearElement.
        reverse: the located object is valid in the reverse direction of the LinearElement.
        both: the located object is valid in both directions.
    ---------
    *Has:
        1...* PositioningNetElement
    *Composition: 
        1...* OrderedAssociatedNetElement
    *Remove: (!) 
        Whenever a LinearLocation instance is removed, all related OrderedAssociatedNetElement ... (NOT DEFINED!)          
    """       
    #def __init__(self) -> None:
    #    self.__applicationDirection = ApplicationDirection.NORMAL

    #def __str__(self):
    #    return f'{self.__applicationDirection}'    
    pass

class LinearLocationCoordinate(LinearLocation):
    """
    !Defines the relation between LinearLocation and PositioningSystemCoordinate instances.
    *Derivates from: 
        LinearLocation   
    *Parameters
    ----------
    applicationDirection:-> ApplicationDirection
        normal: the located object is valid in the direction of the LinearElement.
        reverse: the located object is valid in the reverse direction of the LinearElement.
        both: the located object is valid in both directions.
    ---------
    *Has:
        1...* PositioningSystemCoordinate         
    """       
    #def __init__(self) -> None:
    #    self.__applicationDirection = ApplicationDirection.NORMAL

    #def __str__(self):
    #    return f'{self.__applicationDirection}'    
    pass  
    
class AreaLocation(EntityLocation):
    """
    !Defines a set of AssociatedNetElement instances which together represent an area of interest.
    ! Each AssociatedNetElement instance contains attibutes which designate the extent of the related
    ! PositioningNetElement instance using intrinsic coordinates.
    *Derivates from: 
        EntityLocation   
    *Composition: 
        1...* AssociatedNetElement
    *Remove:
        Whenever a AreaLocation instance is removed, all related AssociatedNetElement are removed as well.
    """   
    pass

class AreaLocationCoordinate(LinearLocation):
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