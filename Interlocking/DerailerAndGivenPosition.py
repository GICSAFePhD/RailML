#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Interlocking import DerailerAndPosition
from Interlocking import AssetAndGivenState
from typing import List

class DerailerAndGivenPosition(AssetAndGivenState):
	"""the tuple of references to the derailer and its position plus the level of enforcement"""
	def setRelatedDerailerAndPosition(self, aRelatedDerailerAndPosition : DerailerAndPosition):
		self._relatedDerailerAndPosition = aRelatedDerailerAndPosition

	def getRelatedDerailerAndPosition(self) -> DerailerAndPosition:
		return self._relatedDerailerAndPosition

	def __init__(self):
		self._relatedDerailerAndPosition : DerailerAndPosition = None
		# @AssociationType Interlocking.DerailerAndPosition
		# @AssociationMultiplicity 1
		# """the tuple of references to the derailer and its position"""

