#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import Name
from RailML.RailTopoModel import RTM_BaseObject
from typing import List

class RTM_NamedResource(RTM_BaseObject.RTM_BaseObject):
	def __init__(self):
		self.___name : Name = None
		# @AssociationType Common.Name*
		# @AssociationMultiplicity 0..*

