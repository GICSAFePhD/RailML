#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tRef
from typing import List

#class RTM_PositioningSystemCoordinate(object): # NO SE XQ CON ESTA HERENCIA SE ROMPE
class RTM_PositioningSystemCoordinate():    
	def __init__(self):
		self.___positioningSystemRef : tRef = None
		# @AssociationType Common.tRef

