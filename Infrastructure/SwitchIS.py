#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common.tRef import tRef
from RailML.Infrastructure.tSwitchType import tSwitchType
from RailML.Infrastructure.tCourse import tCourse
from RailML.Infrastructure.SwitchCrossingBranch import SwitchCrossingBranch
from RailML.Infrastructure.TrackNode import TrackNode
from typing import List

class SwitchIS(TrackNode):
	def setBelongsToParent(self, aBelongsToParent : tRef):
		self.___belongsToParent = aBelongsToParent

	def getBelongsToParent(self) -> tRef:
		return self.___belongsToParent

	def setType(self, aType : tSwitchType):
		self.___type = aType

	def getType(self) -> tSwitchType:
		return self.___type

	def setContinueCourse(self, aContinueCourse : tCourse):
		self.___continueCourse = aContinueCourse

	def getContinueCourse(self) -> tCourse:
		return self.___continueCourse

	def setBranchCourse(self, aBranchCourse : tCourse):
		self.___branchCourse = aBranchCourse

	def getBranchCourse(self) -> tCourse:
		return self.___branchCourse

	def setBasedOnTemplate(self, aBasedOnTemplate : tRef):
		self.___basedOnTemplate = aBasedOnTemplate

	def getBasedOnTemplate(self) -> tRef:
		return self.___basedOnTemplate

	def setLeftBranch(self, aLeftBranch : SwitchCrossingBranch):
		self._leftBranch = aLeftBranch

	def getLeftBranch(self) -> SwitchCrossingBranch:
		return self._leftBranch

	def setRightBranch(self, *aRightBranch : SwitchCrossingBranch):
		self._rightBranch = aRightBranch

	def getRightBranch(self) -> SwitchCrossingBranch:
		return self._rightBranch

	def setStraightBranch(self, *aStraightBranch : SwitchCrossingBranch):
		self._straightBranch = aStraightBranch

	def getStraightBranch(self) -> SwitchCrossingBranch:
		return self._straightBranch

	def setTurningBranch(self, aTurningBranch : SwitchCrossingBranch):
		self._turningBranch = aTurningBranch

	def getTurningBranch(self) -> SwitchCrossingBranch:
		return self._turningBranch

	def __init__(self):
		self.___belongsToParent : tRef = None
		"""reference to the one an only parent switch of this switch (to be used at switch crossings)"""
		self.___type : tSwitchType = None
		# @AssociationType Infrastructure.tSwitchType
		# """type of the switch"""
		self.___continueCourse : tCourse = None
		"""defines the switch main track route (as seen from begin of switch, application direction)"""
		self.___branchCourse : tCourse = None
		# @AssociationType Infrastructure.tCourse
		# @AssociationType Infrastructure.tCourse
		# """defines the switch branching track route (as seen from begin of switch, application direction)"""
		self.___basedOnTemplate : tRef = None
		# @AssociationType Common.tRef
		# @AssociationType Common.tRef
		# """reference to a generic switch"""
		self._leftBranch : SwitchCrossingBranch = None
		"""left branch of the switch as seen from switch begin (application direction)"""
		self._rightBranch : SwitchCrossingBranch = None
		# @AssociationType Infrastructure.SwitchCrossingBranch*
		# @AssociationMultiplicity 0..2
		# """right branch of the switch as seen from switch begin (application direction)"""
		self._straightBranch : SwitchCrossingBranch = None
		# @AssociationType Infrastructure.SwitchCrossingBranch*
		# @AssociationMultiplicity 0..2
		# """only for switch crossings: straight branch"""
		self._turningBranch : SwitchCrossingBranch = None
		# @AssociationType Infrastructure.SwitchCrossingBranch
		# @AssociationMultiplicity 0..1
		# @AssociationType Infrastructure.SwitchCrossingBranch
		# @AssociationMultiplicity 0..1
		# """only for switch crossings: turning branch"""

