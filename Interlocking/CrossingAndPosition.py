#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import tCrossingPosition, EntityILref, AssetAndState
from typing import List

class CrossingAndPosition(AssetAndState.AssetAndState):
	"""Tuple of crossing element and its (logical) position."""
	@property
	def InPosition(self) -> tCrossingPosition:
		return self.___inPosition
	@property
	def RefersToCrossing(self) -> EntityILref:
		return self.___refersToCrossing

	@InPosition.setter
	def InPosition(self, aInPosition : tCrossingPosition):
		self.___inPosition = aInPosition
	@RefersToCrossing.setter
	def RefersToCrossing(self, aRefersToCrossing : EntityILref):
		self.___refersToCrossing = aRefersToCrossing


	def __init__(self):
		self.___inPosition : tCrossingPosition = tCrossingPosition.tCrossingPosition()
		# @AssociationType Interlocking.tCrossingPosition
		# """The position the crossing is in."""
		self.___refersToCrossing : EntityILref = EntityILref.EntityILref()
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# """The reference to the crossing."""

