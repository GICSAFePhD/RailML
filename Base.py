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
        return f'{self.id}|{self.name}|{self.validTo}|{self.validFrom}'        
        
class Network(BaseObject):
    """ 
    !Defines the network being considered. It includes all resources that compose it (all Levels included), 
    !inter alia the topological, structural and positional properties exhibited by any railway network
    *Derivates
    ---------
    Father: BaseObject
    Described in:
        1...* LevelNetwork
        0...* NetworkResource   
    *Remove
    ------    
    Whenever a Network instance is removed, all related LevelNetwork and NetworkResource are removed.   
    *Method
    ------
    add_levelNetwork(self,id,name,validTo,validFrom):
        Create a LevelNetwork
        Add it to list in Network
    add_networkResource(self,id,name,validTo,validFrom):
        Create a NetworkResource
        Add it to list in Network
    """
    def __del__(self):  
        # Removing levelNetwork and networkResource Objects
        print('Removing all LevelNetwork and NetworkResource')
        self.levelNetwork.clear()
        self.networkResource.clear()
    
    def __str__(self):
        print(f'Network:{self.id}|{self.name}|{self.validTo}|{self.validFrom}')
        if (hasattr(self,'levelNetwork')):
            for i in self.levelNetwork:
                print(f'LevelNetwork:{i}')
        if (hasattr(self,'networkResource')):        
            for i in self.networkResource:
                print(f'NetworkResource:{i}')
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
        self.add_levelNetwork(id,name,validTo,validFrom,self.networkResource)
    
    def add_levelNetwork(self,id,name,validTo,validFrom,networkResource): 
        
        #TODO: Deberia tener UN LevelNetwork, lo que es multiple son los ResourceNetwork!!!
        
        # If not levelNetwork in Network 
        if (not hasattr(self,'levelNetwork')):
            # Create the new attribute levelNetwork
            self.levelNetwork = []
        # Create the object LevelNetwork with the parameters
        levelNetwork = LevelNetwork(id,name,validTo,validFrom)
        
        # If not networkResource in levelNetwork
        if (not hasattr(levelNetwork,'networkResource')):
            # Create the new attribute networkResource
            levelNetwork.networkResource = []
        # Associate the networkResource object to the levelNetwork object
        levelNetwork.networkResource = networkResource
        
        # Append the object to the list
        self.levelNetwork.append(levelNetwork)
        
class LevelNetwork(BaseObject):
    """ 
    !Defines a consistent "view" of a Network at a certain level of granularity. 
    !An instance of this class therefore includes all resources that are required
    !to define the corresponding level (e.g. micro/track, or macro/line).
    
    *Derivates
    ---------
    Father: BaseObject
    Belongs to:
        1 Network 
    """
    def __del__(self):  
        print('Removing LevelNetwork')
    
class NetworkResource(BaseObject):
    """ 
    !Define every object of the network, qualified as a resource.
    *Derivates
    ---------
    Father: BaseObject
    Belongs to:
        1 Network
    """
    def __del__(self):  
        print('Removing NetworkResource')