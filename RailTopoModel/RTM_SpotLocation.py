#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tRef, tLengthM
from RailML.Infrastructure import tApplicationDirection
from RailML.RailTopoModel import RTM_LinearCoordinate, RTM_GeometricCoordinate, RTM_EntityLocation
from typing import List

#class RTM_SpotLocation(RTM_EntityLocation): #TODO CON ESTA HERENCIA SE ROMPE
class RTM_SpotLocation():
	def __init__(self):
		self.___netElementRef : tRef = None
		# @AssociationType Common.tRef
		# """reference to a railway topology <netElement> element"""
		self.___intrinsicCoord : complex = None
		"""location on the <netElement> in normalized form (value in range 0..1)"""
		self.___applicationDirection : tApplicationDirection = None
		# @AssociationType schemas.3.1.tApplicationDirection
		# """direction in which the element is applied, related to the orientation of the <netElement>"""
		self.___pos : tLengthM = None
		# @AssociationType Common.tLengthM
		self._linearCoordinate : RTM_LinearCoordinate = None
		# @AssociationType Infrastructure.RTM.RTM_LinearCoordinate
		# @AssociationMultiplicity 0..1
		self._geometricCoordinate : RTM_GeometricCoordinate = None
		# @AssociationType Infrastructure.RTM.RTM_GeometricCoordinate
		# @AssociationMultiplicity 0..1

