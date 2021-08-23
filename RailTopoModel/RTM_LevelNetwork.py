#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import tDescriptionLevel
from RailML.Common import tElementWithIDref
from RailML.RailTopoModel import RTM_BaseObject
from typing import List

class RTM_LevelNetwork(RTM_BaseObject.RTM_BaseObject):
	def __init__(self):
		self.___descriptionLevel : tDescriptionLevel = None
		# @AssociationType schemas.3.1.tDescriptionLevel
		self._networkResource : tElementWithIDref = None
		# @AssociationType Common.tElementWithIDref*
		# @AssociationMultiplicity 0..*

