#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Interlocking import tProtectingSideList
from Interlocking import SwitchAndGivenPosition
from Interlocking import EntityIL
from typing import List

class SwitchInPosition(EntityIL):
	"""reference to any switch and its position inside or outside the restricted area required for use and/or protection"""
	def setProtectingSide(self, aProtectingSide : tProtectingSideList):
		self.___protectingSide = aProtectingSide

	def getProtectingSide(self) -> tProtectingSideList:
		return self.___protectingSide

	def setGivenPosition(self, aGivenPosition : SwitchAndGivenPosition):
		self._givenPosition = aGivenPosition

	def getGivenPosition(self) -> SwitchAndGivenPosition:
		return self._givenPosition

	def __init__(self):
		self.___protectingSide : tProtectingSideList = None
		# @AssociationType Interlocking.tProtectingSideList
		# """indication whether the required position is for protection of the area from inside or outside"""
		self._givenPosition : SwitchAndGivenPosition = None
		# @AssociationType Interlocking.SwitchAndGivenPosition
		# @AssociationMultiplicity 1
		# """the tuple of references to the switch and its position plus the level of enforcement"""

