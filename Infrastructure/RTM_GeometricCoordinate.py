#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import RTM_PositioningSystemCoordinate
from typing import List

#class RTM_GeometricCoordinate(RTM_PositioningSystemCoordinate): # NO SE XQ CON ESTA HERENCIA SE ROMPE
class RTM_GeometricCoordinate():    
	def __init__(self):
		self.___x : complex = None
		self.___y : complex = None
		self.___z : complex = None

