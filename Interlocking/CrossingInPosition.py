#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking.tProtectingSideList import tProtectingSideList
from RailML.Interlocking.CrossingAndGivenPosition import CrossingAndGivenPosition
from RailML.Interlocking.EntityIL import EntityIL
from typing import List

class CrossingInPosition(EntityIL):
	"""reference to any movable crossing and its position inside or outside the restricted area required for use and/or protection"""
	def setProtectingSide(self, aProtectingSide : tProtectingSideList):
		self.___protectingSide = aProtectingSide

	def getProtectingSide(self) -> tProtectingSideList:
		return self.___protectingSide

	def setGivenPosition(self, aGivenPosition : CrossingAndGivenPosition):
		self._givenPosition = aGivenPosition

	def getGivenPosition(self) -> CrossingAndGivenPosition:
		return self._givenPosition

	def __init__(self):
		self.___protectingSide : tProtectingSideList = None
		# @AssociationType Interlocking.tProtectingSideList
		# """indication whether the required position is for protection of the area from inside or outside"""
		self._givenPosition : CrossingAndGivenPosition = None
		# @AssociationType Interlocking.CrossingAndGivenPosition
		# @AssociationMultiplicity 1
		# """the tuple of references to the movable crossing and its position plus the level of enforcement"""

