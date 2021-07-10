import sys
sys.path.append('.')
from RailML.Base import *
#from RailML.Topology import *
#from RailML.NetEntity import *
#from RailML.PositioningSystem import *


# x = Network()

#y1 = NetworkResource()
#y2 = NetworkResource()
#y1.associateNetwork(x)
#y2.associateNetwork(x)

#z = LevelNetwork(level = "Micro")
#z.associateNetwork(x)
#z.associateNetworkResources(y1)
#z.associateNetworkResources(y2)

#print(x)
#print(y1)
#print(y2)
#print(z)

N = 5

network = Network()
# Create the level network
level = LevelNetwork()
# Associate the level to a network
level.associateNetwork(network)

# Iniciate resources
resources = []

for i in range(N):
    # Create resources
    resources.append(NetworkResource())
    # Associate resources to a network
    resources[i].associateNetwork(network)
    # Associate resources yo a level
    level.associateNetworkResources(resources[i])
