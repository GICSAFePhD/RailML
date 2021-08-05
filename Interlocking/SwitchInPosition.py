#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import tProtectingSideList, SwitchAndGivenPosition, EntityIL
from typing import List

class SwitchInPosition(EntityIL.EntityIL):
	"""reference to any switch and its position inside or outside the restricted area required for use and/or protection"""
	@property
	def ProtectingSide(self) -> tProtectingSideList:
		return self.___protectingSide
	@property
	def GivenPosition(self) -> SwitchAndGivenPosition:
		return self.___givenPosition

	@ProtectingSide.setter
	def ProtectingSide(self, aProtectingSide : tProtectingSideList):
		self.___protectingSide = aProtectingSide
	@GivenPosition.setter
	def GivenPosition(self, aGivenPosition : SwitchAndGivenPosition):
		self.___givenPosition = aGivenPosition

	def __init__(self):
		self.___protectingSide : tProtectingSideList = tProtectingSideList.tProtectingSideList()
		# @AssociationType Interlocking.tProtectingSideList
		# """indication whether the required position is for protection of the area from inside or outside"""
		self.___givenPosition : SwitchAndGivenPosition = SwitchAndGivenPosition.SwitchAndGivenPosition()
		# @AssociationType Interlocking.SwitchAndGivenPosition
		# @AssociationMultiplicity 1
		# """the tuple of references to the switch and its position plus the level of enforcement"""

