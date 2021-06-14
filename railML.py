import sys
sys.path.append('.')
from RailML.Enumerates import *
from RailML.Base import *
from RailML.Topology import *
from RailML.NetEntity import *
from RailML.PositioningSystem import *


x = Network()

x.add_levelNetwork("1","2","3","4")
x.add_networkResource("2","3","4","5")
x.add_levelNetwork("3","4","5","6")

print(x)


