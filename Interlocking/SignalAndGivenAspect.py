#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking.SignalAndAspect import SignalAndAspect
from RailML.Interlocking.AssetAndGivenState import AssetAndGivenState
from typing import List

class SignalAndGivenAspect(AssetAndGivenState):
	"""the tuple of references to the signal and its aspect plus the level of enforcement"""
	def setRelatedSignalAndAspect(self, aRelatedSignalAndAspect : SignalAndAspect):
		self._relatedSignalAndAspect = aRelatedSignalAndAspect

	def getRelatedSignalAndAspect(self) -> SignalAndAspect:
		return self._relatedSignalAndAspect

	def __init__(self):
		self._relatedSignalAndAspect : SignalAndAspect = None
		# @AssociationType Interlocking.SignalAndAspect
		# @AssociationMultiplicity 1
		# """the tuple of references to the signal and its aspect"""

