#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Infrastructure import tVMax
from Common import tElementWithIDref
from Infrastructure import FunctionalInfrastructureEntity
from typing import List

class SpeedSection(FunctionalInfrastructureEntity):
	def setMaxSpeed(self, aMaxSpeed : tVMax):
		self.___maxSpeed = aMaxSpeed

	def getMaxSpeed(self) -> tVMax:
		return self.___maxSpeed

	def setIsTemporary(self, aIsTemporary : long):
		self.___isTemporary = aIsTemporary

	def getIsTemporary(self) -> long:
		return self.___isTemporary

	def setIsSignalized(self, aIsSignalized : long):
		self.___isSignalized = aIsSignalized

	def getIsSignalized(self) -> long:
		return self.___isSignalized

	def setValidForSpeedProfile(self, *aValidForSpeedProfile : tElementWithIDref*):
		self._validForSpeedProfile = aValidForSpeedProfile

	def getValidForSpeedProfile(self) -> tElementWithIDref*:
		return self._validForSpeedProfile

	def __init__(self):
		self.___maxSpeed : tVMax = None
		# @AssociationType Infrastructure.tVMax
		# """maximum permitted speed in the speed section, in [km/h]"""
		self.___isTemporary : long = None
		"""boolean value to indicate whether the speed section is temporary"""
		self.___isSignalized : long = None
		"""indicates whether the speed aspect is shown next to the track by a signal or panel (true) or only in the "driver's timetable" (false)"""
		self._validForSpeedProfile : tElementWithIDref = None
		# @AssociationType Common.tElementWithIDref*
		# @AssociationMultiplicity 0..*
		# """reference the <speedProfile> element(s) for which the <speedSection> shall be valid"""

