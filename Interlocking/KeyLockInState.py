#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking.tProtectingSideList import tProtectingSideList
from RailML.Interlocking.LockAndGivenState import LockAndGivenState
from RailML.Interlocking.EntityIL import EntityIL
from typing import List

class KeyLockInState(EntityIL):
	"""reference to any key lock and its state inside or outside the restricted area required for use and/or protection"""
	def setProtectingSide(self, aProtectingSide : tProtectingSideList):
		self.___protectingSide = aProtectingSide

	def getProtectingSide(self) -> tProtectingSideList:
		return self.___protectingSide

	def setGivenState(self, aGivenState : LockAndGivenState):
		self._givenState = aGivenState

	def getGivenState(self) -> LockAndGivenState:
		return self._givenState

	def __init__(self):
		self.___protectingSide : tProtectingSideList = None
		# @AssociationType Interlocking.tProtectingSideList
		# """indication whether the required state is for protection of the area from inside or outside"""
		self._givenState : LockAndGivenState = None
		# @AssociationType Interlocking.LockAndGivenState
		# @AssociationMultiplicity 1
		# """the tuple of references to the key lock and its state plus the level of enforcement"""

