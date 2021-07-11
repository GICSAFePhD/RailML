#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import tLateralSide, tVerticalSide, RTM_PositioningSystemCoordinate
from typing import List

#class RTM_LinearCoordinate(RTM_PositioningSystemCoordinate): #TODO CON ESTA HERENCIA SE ROMPE!
class RTM_LinearCoordinate():    
	def __init__(self):
		self.___lateralDistance : complex = None
		"""absolute value of the lateral offset in unit specified by the referenced positioning system"""
		self.___measure : complex = None
		self.___verticalDistance : complex = None
		"""absolute value of the lateral offset in unit specified by the referenced positioning system"""
		self.___lateralSide : tLateralSide = None
		# @AssociationType schemas.3.1.tLateralSide
		# """lateral side (left or right) in relation to the topology NetElement (as seen in application direction)"""
		self.___verticalSide : tVerticalSide = None
		# @AssociationType schemas.3.1.tVerticalSide
		# """vertical side (above or under) in relation to the topology NetElement"""

