#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import RTM_AssociatedNetElement, RTM_EntityLocation
from typing import List

#class RTM_AreaLocation(RTM_EntityLocation): #TODO CON ESTA HERENCIA SE ROMPE
class RTM_AreaLocation():
	def __init__(self):
		self._associatedNetElement : RTM_AssociatedNetElement = None
		# @AssociationType Infrastructure.RTM.RTM_AssociatedNetElement*
		# @AssociationMultiplicity 1..*

