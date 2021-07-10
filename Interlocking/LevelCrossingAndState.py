#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Interlocking import tLevelCrossingState
from Interlocking import EntityILref
from Interlocking import AssetAndState
from typing import List

class LevelCrossingAndState(AssetAndState):
	"""A tuple of Level Crossing and its position."""
	def setInState(self, aInState : tLevelCrossingState):
		self.___inState = aInState

	def getInState(self) -> tLevelCrossingState:
		return self.___inState

	def setRefersToLevelCrossing(self, aRefersToLevelCrossing : EntityILref):
		self._refersToLevelCrossing = aRefersToLevelCrossing

	def getRefersToLevelCrossing(self) -> EntityILref:
		return self._refersToLevelCrossing

	def __init__(self):
		self.___inState : tLevelCrossingState = None
		# @AssociationType Interlocking.tLevelCrossingState
		# """The state the level crossing has."""
		self._refersToLevelCrossing : EntityILref = None
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# """The reference to the level crossing."""

