#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tElementWithIDref
from RailML.Infrastructure import tVMax, FunctionalInfrastructureEntity
from typing import List, NewType
Long = NewType("Long", int)

class SpeedSection(FunctionalInfrastructureEntity.FunctionalInfrastructureEntity):
	@property
	def MaxSpeed(self) -> tVMax:
		return self.___maxSpeed
	@property
	def IsTemporary(self) -> Long:
		return self.___isTemporary
	@property
	def IsSignalized(self) -> Long:
		return self.___isSignalized
	@property
	def ValidForSpeedProfile(self) -> tElementWithIDref:
		return self.___validForSpeedProfile

	@MaxSpeed.setter
	def MaxSpeed(self, aMaxSpeed : tVMax):
		self.___maxSpeed = aMaxSpeed
	@IsTemporary.setter
	def IsTemporary(self, aIsTemporary : Long):
		self.___isTemporary = aIsTemporary
	@IsSignalized.setter
	def IsSignalized(self, aIsSignalized : Long):
		self.___isSignalized = aIsSignalized
	@ValidForSpeedProfile.setter
	def ValidForSpeedProfile(self, aValidForSpeedProfile : tElementWithIDref):
		self.___validForSpeedProfile = aValidForSpeedProfile

	def create_ValidForSpeedProfile(self):
		if self.ValidForSpeedProfile == None:
			self.ValidForSpeedProfile = []
		self.ValidForSpeedProfile.append(tElementWithIDref.tElementWithIDref())

	def __init__(self):
		super().__init__()
		self.___maxSpeed : tVMax = None
		# @AssociationType Infrastructure.tVMax
		# """maximum permitted speed in the speed section, in [km/h]"""
		self.___isTemporary : Long = None
		"""boolean value to indicate whether the speed section is temporary"""
		self.___isSignalized : Long = None
		"""indicates whether the speed aspect is shown next to the track by a signal or panel (true) or only in the "driver's timetable" (false)"""
		self.___validForSpeedProfile : tElementWithIDref = None
		# @AssociationType Common.tElementWithIDref*
		# @AssociationMultiplicity 0..*
		# """reference the <speedProfile> element(s) for which the <speedSection> shall be valid"""

