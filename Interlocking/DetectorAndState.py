#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking.tDetectorStates import tDetectorStates
from RailML.Interlocking.EntityILref import EntityILref
from RailML.Interlocking.AssetAndState import AssetAndState
from typing import List

class DetectorAndState(AssetAndState):
	"""The tuple of reference to a detector and its state."""
	def setInState(self, aInState : tDetectorStates):
		self.___inState = aInState

	def getInState(self) -> tDetectorStates:
		return self.___inState

	def setRefersToDetector(self, aRefersToDetector : EntityILref):
		self._refersToDetector = aRefersToDetector

	def getRefersToDetector(self) -> EntityILref:
		return self._refersToDetector

	def __init__(self):
		self.___inState : tDetectorStates = None
		# @AssociationType Interlocking.tDetectorStates
		# """The state of the particular detector."""
		self._refersToDetector : EntityILref = None
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# """The reference to the particular detector."""

