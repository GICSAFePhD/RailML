#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import DetectorAndGivenState, EntityIL
from typing import List

class DetectorInState(EntityIL.EntityIL):
	"""reference to any detector and its state inside or outside the restricted area required for use"""
	@property
	def GivenState(self) -> DetectorAndGivenState:
		return self.___givenState
	
	@GivenState.setter
	def GivenState(self, aGivenState : DetectorAndGivenState):
		self.___givenState = aGivenState

	def __init__(self):
		self.___givenState : DetectorAndGivenState = DetectorAndGivenState.DetectorAndGivenState()
		# @AssociationType Interlocking.DetectorAndGivenState
		# @AssociationMultiplicity 1
		# """the tuple of references to the detector and its state plus the level of enforcement"""

