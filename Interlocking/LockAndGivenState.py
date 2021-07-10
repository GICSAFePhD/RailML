#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Interlocking import LockAndState
from Interlocking import AssetAndGivenState
from typing import List

class LockAndGivenState(AssetAndGivenState):
	"""the tuple of references to the key lock and its state plus the level of enforcement"""
	def setRelatedLockAndState(self, aRelatedLockAndState : LockAndState):
		self._relatedLockAndState = aRelatedLockAndState

	def getRelatedLockAndState(self) -> LockAndState:
		return self._relatedLockAndState

	def __init__(self):
		self._relatedLockAndState : LockAndState = None
		# @AssociationType Interlocking.LockAndState
		# @AssociationMultiplicity 1
		# """the tuple of references to the key lock and its state"""

