#!/usr/bin/python
# -*- coding: UTF-8 -*-
from schemas.3.1 import tDescriptionLevel
from Common import tElementWithIDref
from Infrastructure.RTM import RTM_BaseObject
from typing import List

class RTM_LevelNetwork(RTM_BaseObject):
	def __init__(self):
		self.___descriptionLevel : tDescriptionLevel = None
		# @AssociationType schemas.3.1.tDescriptionLevel
		self._networkResource : tElementWithIDref = None
		# @AssociationType Common.tElementWithIDref*
		# @AssociationMultiplicity 0..*

