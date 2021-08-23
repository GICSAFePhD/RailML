#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.RailTopoModel import RTM_AreaLocation, RTM_LinearLocation, RTM_SpotLocation, RTM_NetEntity
from typing import List

#class RTM_LocatedNetEntity(RTM_NetEntity): #TODO CON ESTA HERENCIA SE ROMPE
class RTM_LocatedNetEntity():    
	def __init__(self):
		self._areaLocation : RTM_AreaLocation = None
		# @AssociationType Infrastructure.RTM.RTM_AreaLocation*
		# @AssociationMultiplicity 0..*
		self._linearLocation : RTM_LinearLocation = None
		# @AssociationType Infrastructure.RTM.RTM_LinearLocation*
		# @AssociationMultiplicity 0..*
		self._spotLocation : RTM_SpotLocation = None
		# @AssociationType Infrastructure.RTM.RTM_SpotLocation*
		# @AssociationMultiplicity 0..*

