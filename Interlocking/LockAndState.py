#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking.tLockState import tLockState
from RailML.Interlocking.EntityILref import EntityILref
from RailML.Interlocking.AssetAndState import AssetAndState
from typing import List

class LockAndState(AssetAndState):
	"""The tuple of Masterlock/KeyReleaseInstrument and its states"""
	def setInState(self, aInState : tLockState):
		self.___inState = aInState

	def getInState(self) -> tLockState:
		return self.___inState

	def setRefersToKeyLock(self, aRefersToKeyLock : EntityILref):
		self._refersToKeyLock = aRefersToKeyLock

	def getRefersToKeyLock(self) -> EntityILref:
		return self._refersToKeyLock

	def __init__(self):
		self.___inState : tLockState = None
		# @AssociationType Interlocking.tLockState
		# """The state the key release instrument has."""
		self._refersToKeyLock : EntityILref = None
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# """The reference to the Masterlock or Keylock."""

