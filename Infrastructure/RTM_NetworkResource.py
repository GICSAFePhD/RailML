#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import RTM_Validity, RTM_NamedResource
from typing import List

#class RTM_NetworkResource(RTM_NamedResource): #TODO CON ESTA HERENCIA SE ROMPE!
class RTM_NetworkResource():
	def __init__(self):
		self._isValid : RTM_Validity = None
		# @AssociationType Infrastructure.RTM.RTM_Validity*
		# @AssociationMultiplicity 0..*

