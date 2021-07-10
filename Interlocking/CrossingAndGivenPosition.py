#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Interlocking import CrossingAndPosition
from Interlocking import AssetAndGivenState
from typing import List

class CrossingAndGivenPosition(AssetAndGivenState):
	"""the tuple of references to the movable crossing and its position plus the level of enforcement"""
	def setRelatedCrossingAndPosition(self, aRelatedCrossingAndPosition : CrossingAndPosition):
		self._relatedCrossingAndPosition = aRelatedCrossingAndPosition

	def getRelatedCrossingAndPosition(self) -> CrossingAndPosition:
		return self._relatedCrossingAndPosition

	def __init__(self):
		self._relatedCrossingAndPosition : CrossingAndPosition = None
		# @AssociationType Interlocking.CrossingAndPosition
		# @AssociationMultiplicity 1
		# """the tuple of references to the movable crossing and its position"""

