#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking.tProtectingSideList import tProtectingSideList
from RailML.Interlocking.DerailerAndGivenPosition import DerailerAndGivenPosition
from RailML.Interlocking.EntityIL import EntityIL
from typing import List

class DerailerInPosition(EntityIL):
	"""reference to any derailer and its position inside or outside the restricted area required for use and/or protection"""
	def setProtectingSide(self, aProtectingSide : tProtectingSideList):
		self.___protectingSide = aProtectingSide

	def getProtectingSide(self) -> tProtectingSideList:
		return self.___protectingSide

	def setGivenPosition(self, aGivenPosition : DerailerAndGivenPosition):
		self._givenPosition = aGivenPosition

	def getGivenPosition(self) -> DerailerAndGivenPosition:
		return self._givenPosition

	def __init__(self):
		self.___protectingSide : tProtectingSideList = None
		# @AssociationType Interlocking.tProtectingSideList
		# """indication whether the required position is for protection of the area from inside or outside"""
		self._givenPosition : DerailerAndGivenPosition = None
		# @AssociationType Interlocking.DerailerAndGivenPosition
		# @AssociationMultiplicity 1
		# """the tuple of references to the derailer and its position plus the level of enforcement"""

