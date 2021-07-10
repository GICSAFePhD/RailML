from RailML.Enumerates import LrsMethod
from RailML.Base import BaseObject,NetworkResource

class PositioningSystem(BaseObject):
    """ 
    !Defines the generic concept of a positining system.
    *Derivates from: 
        BaseObject    
    *Has: 
        1...* Relation
    """

class LinearPositioningSystem(PositioningSystem):
    """ 
    !Defines a PositioningSystem where a "line of reference" together with a single number allows a location
    ! within a railway network to be defined.In railway business a "line of reference" is very often represented 
    ! with a line number or a track number together with a start mileage and an end mileage.
    *Derivates from: 
        PositioningSystem   
    *Parameters
    ----------
    linearReferencingMethod: Method for linear referencing-> LrsMethod
        absolute
        relative
        interpolation
    startMeasure: -> Double
        Value for measurement at the beginning of the LinearPositioningSystem 
    endMeasure: -> Double
        Value for measurement at the end of the LinearPositioningSystem 
    uints: -> String
        Units for measurement (e.g. kilometer, meter, mile)  
    ---------  
    *Composition:
        * LinearAnchorPoint  
    *Remove: 
        Whenever a LinearPositioningSystem instance is removed, all related LinearAnchorPoint are removed.         
    """
    #def __init__(self) -> None:
    #    self.__startMeasure = "Double"
    #    self.__endMeasure = "Double"
    #    self.__linearReferencingMethod = LrsMethod.ABSOLUTE
    #    self.__units = "String"

    #def __str__(self):
    #    return f'{self.__startMeasure}|{self.__endMeasure}|{self.__linearReferencingMethod}|{self.__units}'

class LinearAnchorPoint(NetworkResource):
    """ 
    !Defines an ordered set of named points within a LinearPositioningSystem, which are used to transform
    ! between LRS based locations suitable for field work and locations using intrinsic coordinates.
    ! Each point contains an LRS measure and the distance to next LinearAnchorPoint instance.
    *Derivates from: 
        NetworkResource
    *Parameters
    ----------
    anchorName: -> String
        Name of the LinearAnchorPoint instance which is unique within the given LinearPositioningSystem
    measure: -> Double
        Measure of the Anchor Point within the given LinearPositioningSystem 
    measureToNext: -> Double
        Basis for modified interpolation of location in the interval up to the next LinearAnchorPoint
        of the given LinearPositioningSystem
    ---------      
    *Belongs to: 
        1 LinearPositioningSystem
    """
    #def __init__(self) -> None:
    #    self.__anchorName = "String"
    #    self.__measure = "Double"
    #    self.__measureToNext = "Double"

    #def __str__(self):
    #    return f'{self.__anchorName}|{self.__measure}|{self.__measureToNext}'
    
class GeometricPositioningSystem(PositioningSystem):
    """ 
    !Defines schematic, geographic or geodetic Coordinate Reference Systems which are used to position
    ! NetElement instances or NetEntity instances. In the context of RailTopoModel, GeometricPositioningSystem
    ! instances are used to support the transformation between intrinsic locations and geometric coordinates.
    *Derivates from: 
        PositioningSystem
    *Parameters
    ----------
    crsDefinition: -> String
        Coordinate Reference System.
    ----------      
    *Belongs to: 
        1 LinearPositioningSystem
    """
    #def __init__(self) -> None:
    #    self.__crsDefinition = "String"

    #def __str__(self):
    #    return f'{self.__crsDefinition}'

class PositioningSystemCoordinate():
    """ 
    !Defines the generic concept of a coordinate in a positioning system that is used to specify locations
    ! for NetEntity, PositioningNetElement, and all other objects of the network. These coordinates are
    ! either expressed as GeometricCoordinate, or LinearCoordinate, or any future type of coordinate.
    *Derivates from: 
        None
    """
    pass

class IntrinsicCoordinate():
    """ 
    !Defines a coordinate which is used to specify locations in reference to NetElements instances. An intrinsic
    ! coordinate may have an arbitrary real number in inverval [0,1] of associated PositioningSystemCoordinate
    ! instances. 0 and 1 correspond to the extremities of the element.
    *Derivates from: 
        None
    *Parameters
    ----------
    intrinsicCoord: -> Double
        Location in reference to the chosen NetElement, given as value in the interval from 0 to 1.
    ----------
    *Belongs to:
        1 AssociatedPositioningSystem
    *Has:
        0...* PositioningSystemCoordinate
    """
    #def __init__(self) -> None:
    #    self.__intrinsicCoord = "Double"

    #def __str__(self):
    #    return f'{self.__intrinsicCoord}'
    
class LinearCoordinate(PositioningSystemCoordinate):
    """ 
    !Defines a location in rerefence to a given LinearPositioningSystem.
    *Derivates from: 
        PositioningSystemCoordinate
    *Parameters
    ----------
    lateralOffset: -> Double
        Distance perpendicular to the "line of reference"-
    measure: -> Double
        position at the "line of reference" (possibly adjusted to local anomalies usin LinearAnchorPosition).
    verticalOffset: -> Double
        Height above the "line of reference" at the position defined by "measure".
    ----------
    *Has:
        1 LinearPositioningSystem
    """
    #def __init__(self) -> None:
    #    self.__lateralOffset = "Double"
    #    self.__verticalOffset = "Double"
    #    self.__measure = "Double"

    #def __str__(self):
    #    return f'{self.__lateralOffset}|{self.__verticalOffset}|{self.__measure}'        
        
class GeometricCoordinate(PositioningSystemCoordinate):
    """ 
    !Defines one coordinate using a GeometricPositioningSystem as reference system. Depending on the
    ! properties of the coordinate system used, a coordinate consists of cartesian or spherical values.
    ! In case of 2D coordinate systems, the attribute z is undefined.
    *Derivates from: 
        PositioningSystemCoordinate
    *Parameters
    ----------
    x: -> Double
        x value of cartesian coordinate, longitude of spherical coordinate.
    y: -> Double
        y value of cartesian coordinate, latitude of spherical coordinate.
    z: -> Double
        z value of cartesian coordinate, altitude of spherical coordinate.
    ----------
    """
    #def __init__(self) -> None:
    #    self.__x = "Double"
    #    self.__y = "Double"
    #    self.__z = "Double"

    #def __str__(self):
    #    return f'{self.__x}|{self.__y}|{self.__z}'
    
class AssociatedPositioningSystem(NetworkResource):
    """ 
    !Defines the relation between a PositioningNetElement instance and a PositioningSystem instance.
    ! The associated set of IntrinsicCoordinate together with the related PositioningSystemCoordinate
    ! instances define the traslation parameters between IntrinsicCoordinate based locations, and 
    ! locations based on external coordinates (LinearLocationCoordinate or SpotLocationCoordinate)
    ! using LinearPositioningSystem or GeometricPositioningSystem as a coordinate system.
    *Derivates from: 
        NetworkResource
    *Belongs to:
        1 PositioningNetElement
    *Composition:
        1...* IntrinsicCoordinate 
    *Has:
        1 PositioningSystem
    """
    pass