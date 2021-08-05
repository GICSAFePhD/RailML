#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import tDetectorStates, EntityILref, AssetAndState
from typing import List

class DetectorAndState(AssetAndState.AssetAndState):
	"""The tuple of reference to a detector and its state."""
	@property
	def InState(self) -> tDetectorStates:
		return self.___inState
	@property
	def RefersToDetector(self) -> EntityILref:
		return self.___refersToDetector

	@InState.setter
	def InState(self, aInState : tDetectorStates):
		self.___inState = aInState
	@RefersToDetector.setter
	def RefersToDetector(self, aRefersToDetector : EntityILref):
		self.___refersToDetector = aRefersToDetector

	def __init__(self):
		self.___inState : tDetectorStates = tDetectorStates.tDetectorStates()
		# @AssociationType Interlocking.tDetectorStates
		# """The state of the particular detector."""
		self.___refersToDetector : EntityILref = EntityILref.EntityILref()
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# """The reference to the particular detector."""

