#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking.tCrossingPosition import tCrossingPosition
from RailML.Interlocking.EntityILref import EntityILref
from RailML.Interlocking.MovableElement import MovableElement
from typing import List

class MovableCrossing(MovableElement):
	"""Crossings are a special item for interlockings as a position is required for them even if there is no really movable item trackside.
	Some crossings, especially high speed ones, have a movable frog to close the gap at the crossing (UK: movable nose crossing, DE: Herzst�ck mit beweglicher Spitze, NL: kruising met beweegbaar puntstuk). Unlike a switch, such a movable frog will not send the train left or right but it does guide the train. Thus the position is essential for avoiding derailment. Do not confound this class with ordinary double or single slip switches. The latter are regarded as two back-to-back switches."""
	def setPreferredPosition(self, aPreferredPosition : tCrossingPosition):
		self.___preferredPosition = aPreferredPosition

	def getPreferredPosition(self) -> tCrossingPosition:
		return self.___preferredPosition

	def setBranchUpLeft(self, aBranchUpLeft : EntityILref):
		self._branchUpLeft = aBranchUpLeft

	def getBranchUpLeft(self) -> EntityILref:
		return self._branchUpLeft

	def setBranchUpRight(self, aBranchUpRight : EntityILref):
		self._branchUpRight = aBranchUpRight

	def getBranchUpRight(self) -> EntityILref:
		return self._branchUpRight

	def setBranchDownLeft(self, aBranchDownLeft : EntityILref):
		self._branchDownLeft = aBranchDownLeft

	def getBranchDownLeft(self) -> EntityILref:
		return self._branchDownLeft

	def setBranchDownRight(self, *aBranchDownRight : EntityILref):
		self._branchDownRight = aBranchDownRight

	def getBranchDownRight(self) -> EntityILref:
		return self._branchDownRight

	def setHasFoulingTrainDetectors(self, aHasFoulingTrainDetectors : EntityILref):
		self._hasFoulingTrainDetectors = aHasFoulingTrainDetectors

	def getHasFoulingTrainDetectors(self) -> EntityILref:
		return self._hasFoulingTrainDetectors

	def __init__(self):
		self.___preferredPosition : tCrossingPosition = None
		# @AssociationType Interlocking.tCrossingPosition
		# """This is the preferred position of the crossing which it is switched to when not in use."""
		self._branchUpLeft : EntityILref = None
		"""Referral to the physical track that connects from upper left side to the crossing."""
		self._branchUpRight : EntityILref = None
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# """Referral to the physical track that connects from upper right side to the crossing."""
		self._branchDownLeft : EntityILref = None
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# """Referral to the physical track that connects from lower left side to the crossing."""
		self._branchDownRight : EntityILref = None
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 0..*
		# """Referral to the physical track that connects from lower right side to the crossing."""
		self._hasFoulingTrainDetectors : EntityILref = None
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# """This is the reference to the train detectors delimiting the TVD section of this crossing, which are too close and cannot guarantee a clear gauge of the set track."""

