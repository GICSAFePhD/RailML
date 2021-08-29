#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tRef
from RailML.Infrastructure import tSwitchType, tCourse, SwitchCrossingBranch, TrackNode
from typing import List

class SwitchIS(TrackNode.TrackNode):
	@property
	def BelongsToParent(self) -> tRef:
		return self.___belongsToParent
	@property
	def Type(self) -> tSwitchType:
		return self.___type
	@property
	def ContinueCourse(self) -> tCourse:
		return self.___continueCourse
	@property
	def BranchCourse(self) -> tCourse:
		return self.___branchCourse
	@property
	def BasedOnTemplate(self) -> tRef:
		return self.___basedOnTemplate
	@property
	def LeftBranch(self) -> SwitchCrossingBranch:
		return self.___leftBranch
	@property
	def RightBranch(self) -> SwitchCrossingBranch:
		return self.___rightBranch
	@property
	def StraightBranch(self) -> SwitchCrossingBranch:
		return self.___straightBranch
	@property
	def TurningBranch(self) -> SwitchCrossingBranch:
		return self.___turningBranch

	@BelongsToParent.setter
	def BelongsToParent(self, aBelongsToParent : tRef):
		self.___belongsToParent = aBelongsToParent
	@Type.setter
	def Type(self, aType : tSwitchType):
		self.___type = aType
	@ContinueCourse.setter
	def ContinueCourse(self, aContinueCourse : tCourse):
		self.___continueCourse = aContinueCourse
	@BranchCourse.setter
	def BranchCourse(self, aBranchCourse : tCourse):
		self.___branchCourse = aBranchCourse
	@BasedOnTemplate.setter
	def BasedOnTemplate(self, aBasedOnTemplate : tRef):
		self.___basedOnTemplate = aBasedOnTemplate
	@LeftBranch.setter
	def LeftBranch(self, *aLeftBranch : SwitchCrossingBranch):
		self.___leftBranch = aLeftBranch
	@RightBranch.setter
	def RightBranch(self, *aRightBranch : SwitchCrossingBranch):
		self.___rightBranch = aRightBranch
	@StraightBranch.setter
	def StraightBranch(self, *aStraightBranch : SwitchCrossingBranch):
		self.___straightBranch = aStraightBranch
	@TurningBranch.setter
	def TurningBranch(self, *aTurningBranch : SwitchCrossingBranch):
		self.___turningBranch = aTurningBranch

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
		self.___leftBranch : SwitchCrossingBranch = None
		"""left branch of the switch as seen from switch begin (application direction)"""
		self.___rightBranch : SwitchCrossingBranch = None
		# @AssociationType Infrastructure.SwitchCrossingBranch*
		# @AssociationMultiplicity 0..2
		# """right branch of the switch as seen from switch begin (application direction)"""
		self.___straightBranch : SwitchCrossingBranch = None
		# @AssociationType Infrastructure.SwitchCrossingBranch*
		# @AssociationMultiplicity 0..2
		# """only for switch crossings: straight branch"""
		self.___turningBranch : SwitchCrossingBranch = None
		# @AssociationType Infrastructure.SwitchCrossingBranch
		# @AssociationMultiplicity 0..1
		# @AssociationType Infrastructure.SwitchCrossingBranch
		# @AssociationMultiplicity 0..1
		# """only for switch crossings: turning branch"""

