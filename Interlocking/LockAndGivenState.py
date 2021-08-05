#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import LockAndState, AssetAndGivenState
from typing import List

class LockAndGivenState(AssetAndGivenState.AssetAndGivenState):
	"""the tuple of references to the key lock and its state plus the level of enforcement"""
	@property
	def RelatedLockAndState(self) -> LockAndState:
		return self.___relatedLockAndState
	
	@RelatedLockAndState.setter
	def RelatedLockAndState(self, aRelatedLockAndState : LockAndState):
		self.___relatedLockAndState = aRelatedLockAndState

	def __init__(self):
		self.___relatedLockAndState : LockAndState = LockAndState.LockAndState()
		# @AssociationType Interlocking.LockAndState
		# @AssociationMultiplicity 1
		# """the tuple of references to the key lock and its state"""

