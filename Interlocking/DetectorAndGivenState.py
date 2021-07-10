#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Interlocking import DetectorAndState
from Interlocking import AssetAndGivenState
from typing import List

class DetectorAndGivenState(AssetAndGivenState):
	"""the tuple of references to the detector and its state plus the level of enforcement"""
	def setRelatedDetectorAndState(self, aRelatedDetectorAndState : DetectorAndState):
		self._relatedDetectorAndState = aRelatedDetectorAndState

	def getRelatedDetectorAndState(self) -> DetectorAndState:
		return self._relatedDetectorAndState

	def __init__(self):
		self._relatedDetectorAndState : DetectorAndState = None
		# @AssociationType Interlocking.DetectorAndState
		# @AssociationMultiplicity 1
		# """the tuple of references to the detector and its state"""

