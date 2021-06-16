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
    def __init__(self, id="123", name="xyz", validTo="01/01/2050", validFrom="01/01/1990") -> None:       
        self.id =  id
        self.name = name
        self.validTo = validTo
        self.validFrom = validFrom   

    def __str__(self):
        return f'[Id:{self.id}|Name:{self.name}|ValidTo:{self.validTo}|ValidFrom:{self.validFrom}]'   
    
    def __del__(self):  
        print(f'Removing {self.__class__.__name__}')

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
    def __del__(self):  
        # Removing levelNetwork and networkResource Objects
        print('Removing all LevelNetwork and NetworkResource')
        self.levelNetwork.clear()
        self.networkResource.clear()
    
    def __str__(self):
        print(f'Network:\n\tId:{self.id}\n\tName:{self.name}\n\tValidTo:{self.validTo}\n\tValidFrom:{self.validFrom}')
        
        if (hasattr(self,'levelNetwork')):
            for i in self.levelNetwork:
                print(f'\tLevelNetwork:descriptionLevel:{i.descriptionLevel}{i}')
        if (hasattr(self,'networkResource')):        
            for i in self.networkResource:
                print(f'\t\tNetworkResource:{i}')
        return ''        

    def add_networkResource(self,id,name,validTo,validFrom):
        # If not networkResource in Network
        if (not hasattr(self,'networkResource')):
            # Create the new attribute networkResource
            self.networkResource = []
        # Create the object NetworkResource with the parameters
        networkResource = NetworkResource(id,name,validTo,validFrom)
        # Append the object to the list
        self.networkResource.append(networkResource)
        # Associate the networkResource to the levelNetwork 
        self.add_levelNetwork(id,name,validTo,validFrom,networkResource)  
    
    def add_levelNetwork(self,id,name,validTo,validFrom,networkResource):        
        # If not levelNetwork in Network 
        if (not hasattr(self,'levelNetwork')):
            # Create the new attribute levelNetwork
            self.levelNetwork = []   
        # Create the object LevelNetwork with the parameters
        levelNetwork = LevelNetwork("ID5","Level1","Mañana","Hoy")  
        # Create attirube descriptionLevel
        levelNetwork.descriptionLevel = "Micro"
        
        # If not networkResource in levelNetwork
        if (not hasattr(levelNetwork,'networkResource')):
            # Create the new attribute networkResource
            levelNetwork.networkResource = []
        
        networkResourceRepeated = False
        # Check if the networkResource is a new one
        for i in levelNetwork.networkResource:
            if( networkResource.id == i.networkResource.id ):
                networkResourceRepeated = True
        
        if (not networkResourceRepeated):       
            # Append the networkResource object to the levelNetwork object list attribute
            levelNetwork.networkResource.append(networkResource)
        
        # Check if the levelNetwork is a new one
        for i in self.levelNetwork:
            if( levelNetwork.id == i.id):
                return
        
        # If it is a new levelNetwork, append it to the list
        self.levelNetwork.append(levelNetwork)

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
        
class NetworkResource(BaseObject):
    """ 
    !Define every object of the network, qualified as a resource.
    *Derivates from: 
        BaseObject
    *Belongs to: 
        1 Network
    """
    