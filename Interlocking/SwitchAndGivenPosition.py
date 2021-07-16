#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking.SwitchAndPosition import SwitchAndPosition
from RailML.Interlocking.AssetAndGivenState import AssetAndGivenState
from typing import List

class SwitchAndGivenPosition(AssetAndGivenState):
	"""the tuple of references to the switch and its position plus the level of enforcement"""
	def setRelatedSwitchAndPosition(self, aRelatedSwitchAndPosition : SwitchAndPosition):
		self._relatedSwitchAndPosition = aRelatedSwitchAndPosition

	def getRelatedSwitchAndPosition(self) -> SwitchAndPosition:
		return self._relatedSwitchAndPosition

	def __init__(self):
		self._relatedSwitchAndPosition : SwitchAndPosition = None
		# @AssociationType Interlocking.SwitchAndPosition
		# @AssociationMultiplicity 1
		# """the tuple of references to the switch and its position"""

