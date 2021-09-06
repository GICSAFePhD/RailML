#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import tCrossingPosition, EntityILref, MovableElement
from typing import List

class MovableCrossing(MovableElement.MovableElement):
	"""Crossings are a special item for interlockings as a position is required for them even if there is no really movable item trackside.
	Some crossings, especially high speed ones, have a movable frog to close the gap at the crossing (UK: movable nose crossing, DE: Herzst�ck mit beweglicher Spitze, NL: kruising met beweegbaar puntstuk). Unlike a switch, such a movable frog will not send the train left or right but it does guide the train. Thus the position is essential for avoiding derailment. Do not confound this class with ordinary double or single slip switches. The latter are regarded as two back-to-back switches."""
	@property
	def PreferredPosition(self) -> tCrossingPosition:
		return self.___preferredPosition
	@property
	def BranchUpLeft(self) -> EntityILref:
		return self.___branchUpLeft
	@property
	def BranchUpRight(self) -> EntityILref:
		return self.___branchUpRight
	@property
	def BranchDownLeft(self) -> EntityILref:
		return self.___branchDownLeft
	@property
	def BranchDownRight(self) -> EntityILref:
		return self.___branchDownRight
	@property
	def HasFoulingTrainDetectors(self) -> EntityILref:
		return self.___hasFoulingTrainDetectors

	@PreferredPosition.setter
	def PreferredPosition(self, aPreferredPosition : tCrossingPosition):
		self.___preferredPosition = aPreferredPosition
	@BranchUpLeft.setter
	def BranchUpLeft(self, *aBranchUpLeft : EntityILref):
		self.___branchUpLeft = aBranchUpLeft
	@BranchUpRight.setter
	def BranchUpRight(self, *aBranchUpRight : EntityILref):
		self.___branchUpRight = aBranchUpRight
	@BranchDownLeft.setter
	def BranchDownLeft(self, *aBranchDownLeft : EntityILref):
		self.___branchDownLeft = aBranchDownLeft
	@BranchDownRight.setter
	def BranchDownRight(self, *aBranchDownRight : EntityILref):
		self.___branchDownRight = aBranchDownRight
	@HasFoulingTrainDetectors.setter
	def HasFoulingTrainDetectors(self, aHasFoulingTrainDetectors : EntityILref):
		self.___hasFoulingTrainDetectors = aHasFoulingTrainDetectors

	def create_BranchUpLeft(self):
		if self.BranchUpLeft == None:
			self.BranchUpLeft = []
		self.BranchUpLeft.append(EntityILref.EntityILref())
	def create_BranchUpRight(self):
		if self.BranchUpRight == None:
			self.BranchUpRight = []
		self.BranchUpRight.append(EntityILref.EntityILref())
	def create_BranchDownLeft(self):
		if self.BranchDownLeft == None:
			self.BranchDownLeft = []
		self.BranchDownLeft.append(EntityILref.EntityILref())
	def create_BranchDownRight(self):
		if self.BranchDownRight == None:
			self.BranchDownRight = []
		self.BranchDownRight.append(EntityILref.EntityILref())
	def create_HasFoulingTrainDetectors(self):
		if self.HasFoulingTrainDetectors == None:
			self.HasFoulingTrainDetectors = []
		self.HasFoulingTrainDetectors.append(EntityILref.EntityILref())

	def __init__(self):
		super().__init__()
		self.___preferredPosition : tCrossingPosition = None
		# @AssociationType Interlocking.tCrossingPosition
		# """This is the preferred position of the crossing which it is switched to when not in use."""
		self.___branchUpLeft : EntityILref = None
		"""Referral to the physical track that connects from upper left side to the crossing."""
		self.___branchUpRight : EntityILref = None
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# """Referral to the physical track that connects from upper right side to the crossing."""
		self.___branchDownLeft : EntityILref = None
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# """Referral to the physical track that connects from lower left side to the crossing."""
		self.___branchDownRight : EntityILref = None
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 0..*
		# """Referral to the physical track that connects from lower right side to the crossing."""
		self.___hasFoulingTrainDetectors : EntityILref = None
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# """This is the reference to the train detectors delimiting the TVD section of this crossing, which are too close and cannot guarantee a clear gauge of the set track."""