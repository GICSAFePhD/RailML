#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Interlocking import LevelCrossingAndState
from Interlocking import AssetAndGivenState
from typing import List

class LevelCrossingAndGivenState(AssetAndGivenState):
	"""the tuple of references to the level crossing and its state plus the level of enforcement"""
	def setRelatedLevelCrossingAndState(self, aRelatedLevelCrossingAndState : LevelCrossingAndState):
		self._relatedLevelCrossingAndState = aRelatedLevelCrossingAndState

	def getRelatedLevelCrossingAndState(self) -> LevelCrossingAndState:
		return self._relatedLevelCrossingAndState

	def __init__(self):
		self._relatedLevelCrossingAndState : LevelCrossingAndState = None
		# @AssociationType Interlocking.LevelCrossingAndState
		# @AssociationMultiplicity 1
		# """the tuple of references to the level crossing and its state"""

