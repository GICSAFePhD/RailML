import uuid, datetime

class BaseObject():
    """ 
    !Defines four properties shared by most of objects in RailTopoModel
    *Parameters
    ----------
    id: Unique identifier -> UUID
    name: Natural designation of the object -> String
    validTo: Point in time when the object is no longer available for functional usage 
        (if empty, then the object is valid since the validFrom date)
    validFrom: Point in time when the object is available for usage for train operations 
        (if empty, then the object is valid till the validTo date)
    *Methods
    -------
    var(self): get var
    var(self,value): set var to value
    """
    def __init__(self, id = uuid.uuid4(), name="xyz", validTo=datetime.date.today(), validFrom=datetime.date.today()):       
        self.___id  = uuid.uuid4()
        self.___name  = name
        self.___validFrom  = datetime.date.today()
        self.___validTo  = datetime.date.today()
        
    @property
    def Id(self):
        return self.___id
    @property
    def Name(self):
        return self.___name
    @property
    def ValidFrom(self):
        return self.___validFrom
    @property
    def ValidTo(self):
        return self.___validTo
    
    @Id.setter
    def Id(self, aId : uuid):
        self.___id = aId
    @Name.setter    
    def Name(self, aName : str):
        self.___name = aName
    @ValidFrom.setter       
    def ValidFrom(self, aValidFrom : datetime): 
        self.___validFrom = aValidFrom 
    @ValidTo.setter     
    def ValidTo(self, aValidTo : datetime):
        self.___validTo = aValidTo    
    
    def __str__(self):  
        return f'{self.__class__.__name__}> [Id:{self.Id}|Name:{self.Name}|ValidTo:{self.ValidTo}|ValidFrom:{self.ValidFrom}]'
    
    #def __del__(self):  
    #    print(f'Removing {self.__class__.__name__}')

class Network(BaseObject):
    """ 
    !Defines the network being considered. It includes all resources that compose it (all Levels included), 
    !inter alia the topological, structural and positional properties exhibited by any railway network
    *Derivates from: 
        BaseObject
    *Composition:
        1...* LevelNetwork
        0...* NetworkResource   
    *Remove: 
        Whenever a Network instance is removed, all related LevelNetwork and NetworkResource are removed.   
    *Method
    ------
    add_levelNetwork(self,id,name,validTo,validFrom):
        Create a LevelNetwork
        Add NetworkResource to list in LevelNetwork
        Add it to list in Network (if it is not repeated)
    add_networkResource(self,id,name,validTo,validFrom):
        Create a NetworkResource
        Add it to list in Network
        Add it to list in LevelNetwork
    """
    def __init__(self):
        BaseObject.__init__(self)
        """# @AssociationMultiplicity 1..*
        # @AssociationKind Composition"""
        self._levels = []
        """# @AssociationMultiplicity 0..*
        # @AssociationKind Composition"""
        self._networkResources = []
	
    def associateLevelNetwork(self,levelNetwork):
        self._levels.append(levelNetwork)
        
    def associateNetworkResources(self,networkResources):
        self._networkResources.append(networkResources)

class LevelNetwork(BaseObject):
    """ 
    !Defines a consistent "view" of a Network at a certain level of granularity. 
    !An instance of this class therefore includes all resources that are required
    !to define the corresponding level (e.g. micro/track, or macro/line).
    
    *Derivates from: 
        BaseObject
    *Belongs to: 
        1 Network 
    *Has: 
        * NetworkResources
    """
    def __init__(self,level = "Micro"):
        super().__init__()
        
        self._levels : Network = []
        """# @AssociationMultiplicity 1"""
        self._networkResources = []
        """# @AssociationMultiplicity *"""
        # Create attirube descriptionLevel
        self._descriptionLevel = level

    def associateNetwork(self,network):
        self._levels.append(network)
        network.associateNetworkResources(self)
    
    def associateNetworkResources(self,networkResource):
        self._networkResources.append(networkResource)
    
    def __str__(self):
        print(super().__str__())
        if (hasattr(self,'_descriptionLevel')):
                print(f'\tdescriptionLevel:{self._descriptionLevel}')  
        if ( hasattr(self,'_levels') and self._levels != [] ):
            for i in self._levels:
                print(f'\t\t{i}')
        if ( hasattr(self,'_networkResources') and self._networkResources != [] ):        
            for i in self._networkResources:
                print(f'\t\t{i}')
        return ''
    
class NetworkResource(BaseObject):
    """ 
    !Defines every object of the network, qualified as a resource.
    *Derivates from: 
        BaseObject
    *Belongs to: 
        1 Network
    """
    
    def __init__(self):
        super().__init__()
        self._networkResources : Network = []
        """# @AssociationMultiplicity 1"""    
        
    def associateNetwork(self,network):
        self._networkResources.append(network)
        network.associateLevelNetwork(self)
        
    def __str__(self):
        print(super().__str__())
        if ( hasattr(self,'_networkResources') and self._networkResources != [] ):        
            for i in self._networkResources:
                print(f'\t\t{i}')
        return ''
