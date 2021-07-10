#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Common import tSpeedKmPerHour
from Common import tRef
from Common import tLengthM
from typing import List

class SwitchCrossingBranch(object):
	def setBranchingSpeed(self, aBranchingSpeed : tSpeedKmPerHour):
		self.___branchingSpeed = aBranchingSpeed

	def getBranchingSpeed(self) -> tSpeedKmPerHour:
		return self.___branchingSpeed

	def setJoiningSpeed(self, aJoiningSpeed : tSpeedKmPerHour):
		self.___joiningSpeed = aJoiningSpeed

	def getJoiningSpeed(self) -> tSpeedKmPerHour:
		return self.___joiningSpeed

	def setNetRelationRef(self, aNetRelationRef : tRef):
		self.___netRelationRef = aNetRelationRef

	def getNetRelationRef(self) -> tRef:
		return self.___netRelationRef

	def setRadius(self, aRadius : tLengthM):
		self.___radius = aRadius

	def getRadius(self) -> tLengthM:
		return self.___radius

	def setLength(self, aLength : tLengthM):
		self.___length = aLength

	def getLength(self) -> tLengthM:
		return self.___length

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

