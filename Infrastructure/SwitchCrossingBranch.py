#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tRef, tSpeedKmPerHour, tLengthM

from typing import List

class SwitchCrossingBranch(object):
	@property
	def BranchingSpeed(self) -> tSpeedKmPerHour:
		return self.___branchingSpeed
	@property
	def JoiningSpeed(self) -> tSpeedKmPerHour:
		return self.___joiningSpeed
	@property
	def NetRelationRef(self) -> tRef:
		return self.___netRelationRef
	@property
	def Radius(self) -> tLengthM:
		return self.___radius
	@property
	def Length(self) -> tLengthM:
		return self.___length

	@BranchingSpeed.setter
	def BranchingSpeed(self, aBranchingSpeed : tSpeedKmPerHour):
		self.___branchingSpeed = aBranchingSpeed
	@JoiningSpeed.setter
	def JoiningSpeed(self, aJoiningSpeed : tSpeedKmPerHour):
		self.___joiningSpeed = aJoiningSpeed
	@NetRelationRef.setter
	def NetRelationRef(self, aNetRelationRef : tRef):
		self.___netRelationRef = aNetRelationRef
	@Radius.setter
	def Radius(self, aRadius : tLengthM):
		self.___radius = aRadius
	@Length.setter
	def Length(self, aLength : tLengthM):
		self.___length = aLength

	def __init__(self):
		self.___branchingSpeed : tSpeedKmPerHour = None
		self.___joiningSpeed : tSpeedKmPerHour = None
		# @AssociationType Common.tSpeedKmPerHour
		# @AssociationType Common.tSpeedKmPerHour
		self.___netRelationRef : tRef = None
		# @AssociationType Common.tRef
		# """reference to the netRelation that defines the navigability at this switch branch"""
		self.___radius : tLengthM = None
		"""radius of the switch branch in metres"""
		self.___length : tLengthM = None
		# @AssociationType Common.tLengthM
		# @AssociationType Common.tLengthM
		# """length of the switch branch in metres"""