#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking.tProtectingSideList import tProtectingSideList
from RailML.Interlocking.SignalAndGivenAspect import SignalAndGivenAspect
from RailML.Interlocking.EntityIL import EntityIL
from typing import List

class SignalWithAspect(EntityIL):
	"""reference to any signal and its aspect inside or outside the restricted area required for use and/or protection"""
	def setProtectingSide(self, aProtectingSide : tProtectingSideList):
		self.___protectingSide = aProtectingSide

	def getProtectingSide(self) -> tProtectingSideList:
		return self.___protectingSide

	def setGivenAspect(self, aGivenAspect : SignalAndGivenAspect):
		self._givenAspect = aGivenAspect

	def getGivenAspect(self) -> SignalAndGivenAspect:
		return self._givenAspect

	def __init__(self):
		self.___protectingSide : tProtectingSideList = None
		# @AssociationType Interlocking.tProtectingSideList
		# """indication whether the required aspect is for protection of the area from inside or outside"""
		self._givenAspect : SignalAndGivenAspect = None
		# @AssociationType Interlocking.SignalAndGivenAspect
		# @AssociationMultiplicity 1
		# """the tuple of references to the signal and its aspect plus the level of enforcement"""

