#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import LevelCrossingAndGivenState, EntityIL
from typing import List

class LevelCrossingInState(EntityIL.EntityIL):
	"""reference to any level crossing and its state inside the restricted area required for use"""
	@property
	def GivenState(self) -> LevelCrossingAndGivenState:
		return self.___givenState
	
	@GivenState.setter
	def GivenState(self, aGivenState : LevelCrossingAndGivenState):
		self.___givenState = aGivenState

	def __init__(self):
		self.___givenState : LevelCrossingAndGivenState = LevelCrossingAndGivenState.LevelCrossingAndGivenState()
		# @AssociationType Interlocking.LevelCrossingAndGivenState
		# @AssociationMultiplicity 1
		# """the tuple of references to the level crossing and its state plus the level of enforcement"""

