#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking.LevelCrossingAndGivenState import LevelCrossingAndGivenState
from RailML.Interlocking.EntityIL import EntityIL
from typing import List

class LevelCrossingInState(EntityIL):
	"""reference to any level crossing and its state inside the restricted area required for use"""
	def setGivenState(self, aGivenState : LevelCrossingAndGivenState):
		self._givenState = aGivenState

	def getGivenState(self) -> LevelCrossingAndGivenState:
		return self._givenState

	def __init__(self):
		self._givenState : LevelCrossingAndGivenState = None
		# @AssociationType Interlocking.LevelCrossingAndGivenState
		# @AssociationMultiplicity 1
		# """the tuple of references to the level crossing and its state plus the level of enforcement"""

