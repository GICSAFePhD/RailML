#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Interlocking import DetectorAndGivenState
from Interlocking import EntityIL
from typing import List

class DetectorInState(EntityIL):
	"""reference to any detector and its state inside or outside the restricted area required for use"""
	def setGivenState(self, aGivenState : DetectorAndGivenState):
		self._givenState = aGivenState

	def getGivenState(self) -> DetectorAndGivenState:
		return self._givenState

	def __init__(self):
		self._givenState : DetectorAndGivenState = None
		# @AssociationType Interlocking.DetectorAndGivenState
		# @AssociationMultiplicity 1
		# """the tuple of references to the detector and its state plus the level of enforcement"""

