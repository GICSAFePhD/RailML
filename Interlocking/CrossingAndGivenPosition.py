#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import CrossingAndPosition, AssetAndGivenState
from typing import List

class CrossingAndGivenPosition(AssetAndGivenState.AssetAndGivenState):
	"""the tuple of references to the movable crossing and its position plus the level of enforcement"""
	@property
	def RelatedCrossingAndPosition(self) -> CrossingAndPosition:
		return self.___relatedCrossingAndPosition
	
	@RelatedCrossingAndPosition.setter
	def RelatedCrossingAndPosition(self, aRelatedCrossingAndPosition : CrossingAndPosition):
		self.___relatedCrossingAndPosition = aRelatedCrossingAndPosition

	def __init__(self):
		self.___relatedCrossingAndPosition : CrossingAndPosition = CrossingAndPosition.CrossingAndPosition()
		# @AssociationType Interlocking.CrossingAndPosition
		# @AssociationMultiplicity 1
		# """the tuple of references to the movable crossing and its position"""

