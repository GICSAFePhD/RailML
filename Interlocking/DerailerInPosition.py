#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import tProtectingSideList, DerailerAndGivenPosition, EntityIL
from typing import List

class DerailerInPosition(EntityIL.EntityIL):
	"""reference to any derailer and its position inside or outside the restricted area required for use and/or protection"""
	@property
	def ProtectingSide(self) -> tProtectingSideList:
		return self.___protectingSide
	@property
	def GivenPosition(self) -> DerailerAndGivenPosition:
		return self.___givenPosition

	@ProtectingSide.setter
	def ProtectingSide(self, aProtectingSide : tProtectingSideList):
		self.___protectingSide = aProtectingSide
	@GivenPosition.setter
	def GivenPosition(self, aGivenPosition : DerailerAndGivenPosition):
		self.___givenPosition = aGivenPosition

	def __init__(self):
		self.___protectingSide : tProtectingSideList = tProtectingSideList.tProtectingSideList()
		# @AssociationType Interlocking.tProtectingSideList
		# """indication whether the required position is for protection of the area from inside or outside"""
		self.___givenPosition : DerailerAndGivenPosition = DerailerAndGivenPosition.DerailerAndGivenPosition()
		# @AssociationType Interlocking.DerailerAndGivenPosition
		# @AssociationMultiplicity 1
		# """the tuple of references to the derailer and its position plus the level of enforcement"""

