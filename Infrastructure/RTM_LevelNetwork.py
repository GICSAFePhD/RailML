#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure.tDescriptionLevel import tDescriptionLevel
from RailML.Common.tElementWithIDref import tElementWithIDref
from RailML.Infrastructure.RTM_BaseObject import RTM_BaseObject
from typing import List

class RTM_LevelNetwork(RTM_BaseObject):
	def __init__(self):
		self.___descriptionLevel : tDescriptionLevel = None
		# @AssociationType schemas.3.1.tDescriptionLevel
		self._networkResource : tElementWithIDref = None
		# @AssociationType Common.tElementWithIDref*
		# @AssociationMultiplicity 0..*

