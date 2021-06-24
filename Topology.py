from RailML.Base import NetworkResource
from RailML.Enumerates import Navigability, Usage

class NetElement(NetworkResource):  # The base class to define nodes in Graph theory
    """ 
    !Defines the base memeber of topology in a conexity graph of a network (at any level)
    *Derivates from: 
        NetworkResource    
    *Has: 
        1...* Relation
    """
class CompositionNetElement(NetElement):    # Assembly of nodes into bigger nodes
    """ 
    !Defines a topological element that aggregates some other topological element from another level 
    !(e.g. a macro element aggregates micro elements)
    *Derivates from: 
        NetElement
    *Composition: 
        0...* ElementPartCollection
    *Remove: 
        Whenever an instance CompositionNetElement is removed, all related ElementPartCollection are removed.      
    """

class Relation(NetworkResource):    # The base class to define edges in Graph theory
    """ 
    !Defines the connexity relation between two NetElements in the connexity graph of the network.
    *Derivates from: 
        NetworkResource
    *Belongs to: 
        1...* NetElement
    *Has:
        1 PositionedRelation (elementA)
        1 PositionedRelation (elementB)
        1...* AssociatedNetElement (netElement)
        1 SpotLocation (netElement)
        1...* LinearLocation (netElement)
    """

class PositionedRelation(Relation):
    """ 
    !Defines an oriented relation between exactly two PositioningNetElements.
    *Derivates from: 
        Relation
    *Parameters
    ----------
    navigability: -> Navigabilty
        AB: It is possible to move a train ONLY from NetElement "A" to NetElement "B". 
        BA: It is possible to move a train ONLY from NetElement "B" to NetElement "A". 
        Both: It is possible to move a train from NetElement "A" to "B" as well as from "B" to "A". 
        None: It is not possible to move a train across this Relation in any direction.
    positionOnA: -> Usage
        0: The Relation is using the start of NetElement "A".
        1: The Relation is using the end of NetElement "A".
    positionOnB: -> Usage
        0: The Relation is using the start of NetElement "B".
        1: The Relation is using the end of NetElement "B".
    ---------    
    *Has: 
        1 PositioningNetElement (elementA)
        1 PositioningNetElement (elementB)
    """
    #def __init__(self) -> None:
    #    self.__navigability = Navigability.NONE
    #    self.__positionOnA = Usage.USING_START
    #    self.__positionOnB = Usage.USING_START

    #def __str__(self):
    #    return f'{self.__navigability}|{self.__positionOnA}|{self.__positionOnB}'

class ElementPartCollection(NetworkResource):
    """ 
    !Defines every object of the network, qualified as a resource.
    *Derivates from: 
        NetworkResource
    *Belongs to: 
        1 CompositionNetElement
    """

class PositioningNetElement(CompositionNetElement):
    """ 
    !Defines a NetElement requiring al least one PositioningSystem, with orientation (carried by IntrinsicCoordinate).
    *Derivates from: 
        CompositionNetElement
    *Composition: 
        1...* AssociatedPositioningSystem
    *Remove: 
        Whenever an instance PositioningNetElement is removed, all related AssociatedPositioningSystem are removed. 
    """

class LinearElement(PositioningNetElement):
    """ 
    !Defines PositiongNetElement instances that are one-dimensional.
    *Derivates from: 
        PositioningNetElement 
    """
    def __del__(self):  
        print('Removing LinearElement')

class NonLinearElement(PositioningNetElement):
    """ 
    !Defines PositiongNetElement instances with no dimensions (spots).
    *Derivates from: 
        PositioningNetElement 
    """
    def __del__(self):  
        print('Removing LinearElement')

class AssociatedNetElement():
    """ 
    !Defines topological structures and location information in relation between NetElement instances 
    ! and in relation between one NetElement intance and location information for NetEntity instances.
    *Derivates from: 
        None  
    *Parameters
    ----------
    intrinsicCoordBegin: -> Double
        Start location of the NetEntity instance in relation to the PositioningNetElement which is used for positioning within the network
    intrinsicCoordEnd: -> Double
        End location of the NetEntity instance in relation to the PositioningNetElement which is used for positioning within the network
    KeepsOrientation: -> Bool
        Child LinearElement keeps same Orientation as parent LinearElement
        0 (False): Orientation is not relevant.
        1 (True): Orientation is relevant.
    ---------        
    *Belongs to: 
        1 AreaLocation
    *Has:
        1...* PositioningNetElement (netElement)
    """
    
    #def __init__(self) -> None:
    #    self.__intrinsicCoordBegin = "Double"
    #    self.__intrinsicCoordEnd = "Double"
    #    self.__keepsOrientation = "Bool"

    #def __str__(self):
    #    return f'{self.__intrinsicCoordBegin}|{self.__intrinsicCoordEnd}|{self.__keepsOrientation}'
    
class OrderedAssociatedNetElement(AssociatedNetElement):
    """ 
    !Defines the ordered sequences of AssociatedNetElement instances which together describe 
    ! the completestructure of a LinearLocation instace.
    *Derivates from: 
        AssociatedNetElement  
    *Parameters
    ----------
    sequence: -> Int
    ---------        
    *Belongs to: 
        (No number defined) LinearLocation
    """
    
    def __init__(self) -> None:
        self.__sequence = "Int"

    def __str__(self):
        return f'{self.__sequence}'
    
class OrderedCollection(ElementPartCollection):
    """ 
    !Define a subclass of ElementPartCollection dedicated to ordered NetElements (required to build a route).
    *Parameters
    ----------
    sequence: Sequence of the child element within the ordered collection -> int
    ---------
    *Derivates from: 
        ElementPartCollection
    *Has: 
        1...* NetElement (elementPart (ordered))
    """
    #def __init__(self) -> None:
    #    self.__sequence = "Int"

class UnorderedCollection(ElementPartCollection):
    """ 
    !Define a subclass of ElementPartCollection dedicated to unordered NetElements (bulk list without need for routes).
    *Derivates from: 
        ElementPartCollection
    *Has: 
        1...* NetElement (elementPart (no ordering property))
    """
    #def __init__(self) -> None:
    #    self.__sequence = "Int"

class Trail(LinearElement): # not part of RailTopoModel
    """ 
    !Defines an uninterrupted track between two adjacent switches, or between a switch and an adjacent buffer stop.
    ! "Uninterrupted" means that there are no other switches in that connection.
    ! Can represent nodes at Micro level, according to Graph theory
    *Derivates from: 
        LinearElement 
    """

class SectionOfLine(LinearElement): # not part of RailTopoModel
    """ 
    !Defines a line section between two adjacent Operational Points.
    ! Would be an importan class of nodes to be used at Macro level.
    *Derivates from: 
        LinearElement 
    """

class NetLimit(NonLinearElement): # not part of RailTopoModel
    """ 
    !Defines (NOT DEFINED). Only provided as example of class that may represent a node at Macro level.
    *Derivates from: 
        NonLinearElement 
    """

class OperationalPoint(NonLinearElement): # not part of RailTopoModel
    """ 
    !Defines (NOT DEFINED). Only provided as example of class that may represent a node at Macro level.
    *Derivates from: 
        NonLinearElement 
    """