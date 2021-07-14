#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure.tVMax import tVMax
from RailML.Common.tElementWithIDref import tElementWithIDref
from RailML.Infrastructure.FunctionalInfrastructureEntity import FunctionalInfrastructureEntity
from typing import List

class SpeedSection(FunctionalInfrastructureEntity):
	def setMaxSpeed(self, aMaxSpeed : tVMax):
		self.___maxSpeed = aMaxSpeed

	def getMaxSpeed(self) -> tVMax:
		return self.___maxSpeed

	def setIsTemporary(self, aIsTemporary : int):	#TODO DEFINED AS LONG
		self.___isTemporary = aIsTemporary

	def getIsTemporary(self) -> int:	#TODO DEFINED AS LONG
		return self.___isTemporary

	def setIsSignalized(self, aIsSignalized : int):	#TODO DEFINED AS LONG
		self.___isSignalized = aIsSignalized

	def getIsSignalized(self) -> int:	#TODO DEFINED AS LONG
		return self.___isSignalized

	def setValidForSpeedProfile(self, *aValidForSpeedProfile : tElementWithIDref):
		self._validForSpeedProfile = aValidForSpeedProfile

	def getValidForSpeedProfile(self) -> tElementWithIDref:
		return self._validForSpeedProfile

	def __init__(self):
		self.___maxSpeed : tVMax = None
		# @AssociationType Infrastructure.tVMax
		# """maximum permitted speed in the speed section, in [km/h]"""
		self.___isTemporary : int = None	#TODO DEFINED AS LONG
		"""boolean value to indicate whether the speed section is temporary"""
		self.___isSignalized : int = None	#TODO DEFINED AS LONG
		"""indicates whether the speed aspect is shown next to the track by a signal or panel (true) or only in the "driver's timetable" (false)"""
		self._validForSpeedProfile : tElementWithIDref = None
		# @AssociationType Common.tElementWithIDref*
		# @AssociationMultiplicity 0..*
		# """reference the <speedProfile> element(s) for which the <speedSection> shall be valid"""

