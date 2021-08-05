#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import tProtectingSideList, LockAndGivenState, EntityIL
from typing import List

class KeyLockInState(EntityIL.EntityIL):
	"""reference to any key lock and its state inside or outside the restricted area required for use and/or protection"""
	@property
	def ProtectingSide(self) -> tProtectingSideList:
		return self.___protectingSide
	@property
	def GivenState(self) -> LockAndGivenState:
		return self.___givenState

	@ProtectingSide.setter
	def ProtectingSide(self, aProtectingSide : tProtectingSideList):
		self.___protectingSide = aProtectingSide
	@GivenState.setter
	def GivenState(self, aGivenState : LockAndGivenState):
		self.___givenState = aGivenState

	def __init__(self):
		self.___protectingSide : tProtectingSideList = tProtectingSideList.tProtectingSideList()
		# @AssociationType Interlocking.tProtectingSideList
		# """indication whether the required state is for protection of the area from inside or outside"""
		self.___givenState : LockAndGivenState = LockAndGivenState.LockAndGivenState()
		# @AssociationType Interlocking.LockAndGivenState
		# @AssociationMultiplicity 1
		# """the tuple of references to the key lock and its state plus the level of enforcement"""

