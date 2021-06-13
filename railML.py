# class bebida:
#     def __init__(self,tipo ="ninguno",precio = 0) -> None:
#         __tipo: tipo
#         __precio: precio

#     def elegir_bebida(self,tipo):
#         self.__tipo = tipo
#     def comprar_bebida(self,precio):
#         self.__precio = precio        
#     def __str__(self) -> str:
#         return f'Bebida:{self.__tipo},precio:{self.__precio}'
    
# x = bebida()        
# x.elegir_bebida("coca")
# x.comprar_bebida(5)
    
# print(x)    

import sys
sys.path.append('.')

from RailML.Enumerates import *
from RailML.Base import *
from RailML.Topology import *
from RailML.NetEntity import *
from RailML.PositioningSystem import *


x = PositionedRelation()
print(x)


