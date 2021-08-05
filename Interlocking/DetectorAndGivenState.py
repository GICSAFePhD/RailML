#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import DetectorAndState, AssetAndGivenState
from typing import List

class DetectorAndGivenState(AssetAndGivenState.AssetAndGivenState):
	"""the tuple of references to the detector and its state plus the level of enforcement"""
	@property
	def RelatedDetectorAndState(self) -> DetectorAndState:
		return self.___relatedDetectorAndState
	
	@RelatedDetectorAndState.setter
	def RelatedDetectorAndState(self, aRelatedDetectorAndState : DetectorAndState):
		self.___relatedDetectorAndState = aRelatedDetectorAndState

	def __init__(self):
		self.___relatedDetectorAndState : DetectorAndState = DetectorAndState.DetectorAndState()
		# @AssociationType Interlocking.DetectorAndState
		# @AssociationMultiplicity 1
		# """the tuple of references to the detector and its state"""

