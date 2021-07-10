#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Interlocking import tSwitchPosition
from Interlocking import EntityILref
from Interlocking import SwitchPositionRestriction
from Interlocking import MovableElement
from typing import List

class SwitchIL(MovableElement):
	"""Extends the infrastructure::switch for IXL purposes. The graph model from RailTopoModel allows the definition of connections between tracks. Thus, one can include or exclude connections between tracks. The name SwitchIL is chosen to reconcile US nomenclature and to avoid a naming conflict with infrastructure domain."""
	def setPreferredPosition(self, aPreferredPosition : tSwitchPosition):
		self.___preferredPosition = aPreferredPosition

	def getPreferredPosition(self) -> tSwitchPosition:
		return self.___preferredPosition

	def setHasFoulingTrainDetectors(self, aHasFoulingTrainDetectors : EntityILref):
		self._hasFoulingTrainDetectors = aHasFoulingTrainDetectors

	def getHasFoulingTrainDetectors(self) -> EntityILref:
		return self._hasFoulingTrainDetectors

	def setBranchLeft(self, aBranchLeft : EntityILref):
		self._branchLeft = aBranchLeft

	def getBranchLeft(self) -> EntityILref:
		return self._branchLeft

	def setBranchRight(self, *aBranchRight : EntityILref*):
		self._branchRight = aBranchRight

	def getBranchRight(self) -> EntityILref*:
		return self._branchRight

	def setHasPositionRestriction(self, aHasPositionRestriction : SwitchPositionRestriction):
		self._hasPositionRestriction = aHasPositionRestriction

	def getHasPositionRestriction(self) -> SwitchPositionRestriction:
		return self._hasPositionRestriction

	def __init__(self):
		self.___preferredPosition : tSwitchPosition = None
		# @AssociationType Interlocking.tSwitchPosition
		# """This is the preferred position of the switch which it is switched to when not in use or in case of both positions required for flank protection."""
		self._hasFoulingTrainDetectors : EntityILref = None
		"""This is the reference to any train detection device in infrastructure which is located to close to the switch, i.e. the gauge of the switch is not clear when the associated neighbouring TVD section is occupied."""
		self._branchLeft : EntityILref = None
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# """This is the reference to the underlying track section in infrastructure of the left branch."""
		self._branchRight : EntityILref = None
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 0..*
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 0..*
		# """This is the reference to the underlying track section in infrastructure of the right branch."""
		self._hasPositionRestriction : SwitchPositionRestriction = None
		# @AssociationType Interlocking.SwitchPositionRestriction
		# @AssociationMultiplicity 0..1
		# """It defines the position the switch shall have in dependency of the position of the related element."""

