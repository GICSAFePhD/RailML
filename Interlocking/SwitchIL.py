#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import tSwitchPosition, EntityILref, SwitchPositionRestriction, MovableElement
from typing import List

class SwitchIL(MovableElement.MovableElement):
	"""Extends the infrastructure::switch for IXL purposes. The graph model from RailTopoModel allows the definition of connections between tracks. Thus, one can include or exclude connections between tracks. The name SwitchIL is chosen to reconcile US nomenclature and to avoid a naming conflict with infrastructure domain."""
	@property
	def PreferredPosition(self) -> tSwitchPosition:
		return self.___preferredPosition
	@property
	def HasFoulingTrainDetectors(self) -> EntityILref:
		return self.___hasFoulingTrainDetectors
	@property
	def BranchLeft(self) -> EntityILref:
		return self.___branchLeft
	@property
	def BranchRight(self) -> EntityILref:
		return self.___branchRight
	@property
	def HasPositionRestriction(self) -> SwitchPositionRestriction:
		return self.___hasPositionRestriction

	@PreferredPosition.setter
	def PreferredPosition(self, aPreferredPosition : tSwitchPosition):
		self.___preferredPosition = aPreferredPosition
	@HasFoulingTrainDetectors.setter
	def HasFoulingTrainDetectors(self, aHasFoulingTrainDetectors : EntityILref):
		self.___hasFoulingTrainDetectors = aHasFoulingTrainDetectors
	@BranchLeft.setter
	def BranchLeft(self, aBranchLeft : EntityILref): # TODO *aBranchLeft
		self.___branchLeft = aBranchLeft
	@BranchRight.setter
	def BranchRight(self, aBranchRight : EntityILref): # TODO *aBranchRight
		self.___branchRight = aBranchRight
	@HasPositionRestriction.setter
	def HasPositionRestriction(self, aHasPositionRestriction : SwitchPositionRestriction):
		self.___hasPositionRestriction = aHasPositionRestriction

	def create_HasFoulingTrainDetectors(self):
		if self.HasFoulingTrainDetectors == None:
			self.HasFoulingTrainDetectors = []
		self.HasFoulingTrainDetectors.append(EntityILref.EntityILref())
	def create_BranchLeft(self):
		if self.BranchLeft == None:
			self.BranchLeft = []
		self.BranchLeft.append(EntityILref.EntityILref())
	def create_BranchRight(self):
		if self.BranchRight == None:
			self.BranchRight = []
		self.BranchRight.append(EntityILref.EntityILref())
	def create_HasPositionRestriction(self):
		if self.HasPositionRestriction == None:
			self.HasPositionRestriction = []
		self.HasPositionRestriction.append(SwitchPositionRestriction.SwitchPositionRestriction())

	def __init__(self):
		super().__init__()
		self.___preferredPosition : tSwitchPosition = None
		# @AssociationType Interlocking.tSwitchPosition
		# """This is the preferred position of the switch which it is switched to when not in use or in case of both positions required for flank protection."""
		self.___hasFoulingTrainDetectors : EntityILref = None
		"""This is the reference to any train detection device in infrastructure which is located to close to the switch, i.e. the gauge of the switch is not clear when the associated neighbouring TVD section is occupied."""
		self.___branchLeft : EntityILref = None
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# """This is the reference to the underlying track section in infrastructure of the left branch."""
		self.___branchRight : EntityILref = None
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 0..*
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 0..*
		# """This is the reference to the underlying track section in infrastructure of the right branch."""
		self.___hasPositionRestriction : SwitchPositionRestriction = None
		# @AssociationType Interlocking.SwitchPositionRestriction
		# @AssociationMultiplicity 0..1
		# """It defines the position the switch shall have in dependency of the position of the related element."""