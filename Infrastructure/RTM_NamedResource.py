#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import Name
from RailML.Infrastructure import RTM_BaseObject
from typing import List

#class RTM_NamedResource(RTM_BaseObject): #TODO CON ESTA HERENCIA SE ROMPE!
class RTM_NamedResource():
	def __init__(self):
		self._name : Name = None
		# @AssociationType Common.Name*
		# @AssociationMultiplicity 0..*

