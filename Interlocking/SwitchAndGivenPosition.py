#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import SwitchAndPosition, AssetAndGivenState
from typing import List

class SwitchAndGivenPosition(AssetAndGivenState.AssetAndGivenState):
	"""the tuple of references to the switch and its position plus the level of enforcement"""
	@property
	def RelatedSwitchAndPosition(self) -> SwitchAndPosition:
		return self.___relatedSwitchAndPosition
	
	@RelatedSwitchAndPosition.setter
	def RelatedSwitchAndPosition(self, aRelatedSwitchAndPosition : SwitchAndPosition):
		self.___relatedSwitchAndPosition = aRelatedSwitchAndPosition

	def create_RelatedSwitchAndPosition(self):
		self.RelatedSwitchAndPosition = SwitchAndPosition.SwitchAndPosition()

	def __init__(self):
		super().__init__()
		self.___relatedSwitchAndPosition : SwitchAndPosition = None
		# @AssociationType Interlocking.SwitchAndPosition
		# @AssociationMultiplicity 1
		# """the tuple of references to the switch and its position"""