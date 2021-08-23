#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import tApplicationDirection
from RailML.RailTopoModel import RTM_AssociatedNetElement, RTM_LinearCoordinate, RTM_GeometricCoordinate, RTM_EntityLocation
from typing import List

#class RTM_LinearLocation(RTM_EntityLocation): #TODO CON ESTA HERENCIA SE ROMPE
class RTM_LinearLocation():
	def __init__(self):
		self.___applicationDirection : tApplicationDirection = None
		# @AssociationType schemas.3.1.tApplicationDirection
		# """direction in which the element is applied, related to the orientation of the <netElement>"""
		self._associatedNetElement : RTM_AssociatedNetElement = None
		# @AssociationType Infrastructure.RTM.RTM_AssociatedNetElement*
		# @AssociationMultiplicity 1..*
		self._linearCoordinate : RTM_LinearCoordinate = None
		# @AssociationType Infrastructure.RTM.RTM_LinearCoordinate*
		# @AssociationMultiplicity 0..*
		self._geometricCoordinate : RTM_GeometricCoordinate = None
		# @AssociationType Infrastructure.RTM.RTM_GeometricCoordinate*
		# @AssociationMultiplicity 0..*

