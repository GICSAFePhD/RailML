#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import DerailerAndPosition, AssetAndGivenState
from typing import List

class DerailerAndGivenPosition(AssetAndGivenState.AssetAndGivenState):
	"""the tuple of references to the derailer and its position plus the level of enforcement"""
	@property
	def RelatedDerailerAndPosition(self) -> DerailerAndPosition:
		return self.___relatedDerailerAndPosition
	
	@RelatedDerailerAndPosition.setter
	def RelatedDerailerAndPosition(self, aRelatedDerailerAndPosition : DerailerAndPosition):
		self.___relatedDerailerAndPosition = aRelatedDerailerAndPosition

	def __init__(self):
		self.___relatedDerailerAndPosition : DerailerAndPosition = DerailerAndPosition.DerailerAndPosition()
		# @AssociationType Interlocking.DerailerAndPosition
		# @AssociationMultiplicity 1
		# """the tuple of references to the derailer and its position"""

