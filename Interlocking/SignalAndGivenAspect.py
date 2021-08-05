#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import SignalAndAspect, AssetAndGivenState
from typing import List

class SignalAndGivenAspect(AssetAndGivenState.AssetAndGivenState):
	"""the tuple of references to the signal and its aspect plus the level of enforcement"""
	@property
	def RelatedSignalAndAspect(self) -> SignalAndAspect:
		return self.___relatedSignalAndAspect
	
	@RelatedSignalAndAspect.setter
	def RelatedSignalAndAspect(self, aRelatedSignalAndAspect : SignalAndAspect):
		self.___relatedSignalAndAspect = aRelatedSignalAndAspect

	def __init__(self):
		self.___relatedSignalAndAspect : SignalAndAspect = SignalAndAspect.SignalAndAspect()
		# @AssociationType Interlocking.SignalAndAspect
		# @AssociationMultiplicity 1
		# """the tuple of references to the signal and its aspect"""

