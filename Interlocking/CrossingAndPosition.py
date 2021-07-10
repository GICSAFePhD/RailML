#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Interlocking import tCrossingPosition
from Interlocking import EntityILref
from Interlocking import AssetAndState
from typing import List

class CrossingAndPosition(AssetAndState):
	"""Tuple of crossing element and its (logical) position."""
	def setInPosition(self, aInPosition : tCrossingPosition):
		self.___inPosition = aInPosition

	def getInPosition(self) -> tCrossingPosition:
		return self.___inPosition

	def setRefersToCrossing(self, aRefersToCrossing : EntityILref):
		self._refersToCrossing = aRefersToCrossing

	def getRefersToCrossing(self) -> EntityILref:
		return self._refersToCrossing

	def __init__(self):
		self.___inPosition : tCrossingPosition = None
		# @AssociationType Interlocking.tCrossingPosition
		# """The position the crossing is in."""
		self._refersToCrossing : EntityILref = None
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# """The reference to the crossing."""

