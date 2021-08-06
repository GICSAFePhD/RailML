#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import tLevelCrossingState, EntityILref, AssetAndState
from typing import List

class LevelCrossingAndState(AssetAndState.AssetAndState):
	"""A tuple of Level Crossing and its position."""
	@property
	def InState(self) -> tLevelCrossingState:
		return self.___inState
	@property
	def RefersToLevelCrossing(self) -> EntityILref:
		return self.___refersToLevelCrossing

	@InState.setter
	def InState(self, aInState : tLevelCrossingState):
		self.___inState = aInState
	@RefersToLevelCrossing.setter
	def RefersToLevelCrossing(self, aRefersToLevelCrossing : EntityILref):
		self.___refersToLevelCrossing = aRefersToLevelCrossing

	def __init__(self):
		self.___inState : tLevelCrossingState = tLevelCrossingState.tLevelCrossingState()
		# @AssociationType Interlocking.tLevelCrossingState
		# """The state the level crossing has."""
		self.___refersToLevelCrossing : EntityILref = EntityILref.EntityILref()
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# """The reference to the level crossing."""

