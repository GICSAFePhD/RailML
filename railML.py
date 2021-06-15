import sys
sys.path.append('.')
from RailML.Base import *
from RailML.Topology import *
#from RailML.NetEntity import *
#from RailML.PositioningSystem import *

network = Network()

network.add_networkResource("ID1","cosa_1","01/01/2020","01/01/2030")
network.add_networkResource("ID2","cosa_2","02/01/2020","02/01/2030")
network.add_networkResource("ID3","cosa_3","03/01/2020","03/01/2030")

print(network)

#topology = Topology()
