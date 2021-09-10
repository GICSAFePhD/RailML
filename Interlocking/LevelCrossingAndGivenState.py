#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import LevelCrossingAndState, AssetAndGivenState
from typing import List

class LevelCrossingAndGivenState(AssetAndGivenState.AssetAndGivenState):
	"""the tuple of references to the level crossing and its state plus the level of enforcement"""
	@property
	def RelatedLevelCrossingAndState(self) -> LevelCrossingAndState:
		return self.___relatedLevelCrossingAndState
	
	@RelatedLevelCrossingAndState.setter
	def RelatedLevelCrossingAndState(self, aRelatedLevelCrossingAndState : LevelCrossingAndState):
		self.___relatedLevelCrossingAndState = aRelatedLevelCrossingAndState

	def __init__(self):
		super().__init__()
		self.___relatedLevelCrossingAndState : LevelCrossingAndState = None
		# @AssociationType Interlocking.LevelCrossingAndState
		# @AssociationMultiplicity 1
		# """the tuple of references to the level crossing and its state"""

