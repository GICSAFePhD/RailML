#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import SpeedProfileTilting, SpeedProfileLoad, SpeedProfileBraking, SpeedProfileTrainType, tElementWithIDandName#, aSpeedProfile
from typing import List

class SpeedProfile(tElementWithIDandName.tElementWithIDandName):
	@property
	def SpeedProfileTilting(self) -> SpeedProfileTilting:
		return self.___tilting
	@property
	def SpeedProfileLoad(self) -> SpeedProfileLoad:
		return self.___load
	@property
	def SpeedProfileBraking(self) -> SpeedProfileBraking:
		return self.___braking
	@property
	def SpeedProfileTrainType(self) -> SpeedProfileTrainType:
		return self.___trainType

	@SpeedProfileTilting.setter
	def SpeedProfileTilting(self, aSpeedProfileTilting : SpeedProfileTilting):
		self.___tilting = aSpeedProfileTilting
	@SpeedProfileLoad.setter
	def SpeedProfileLoad(self, aSpeedProfileLoad : SpeedProfileLoad):
		self.___load = aSpeedProfileLoad
	@SpeedProfileBraking.setter
	def SpeedProfileBraking(self, aSpeedProfileBraking : SpeedProfileBraking):
		self.___braking = aSpeedProfileBraking
	@SpeedProfileTrainType.setter
	def SpeedProfileTrainType(self, aSpeedProfileTrainType : SpeedProfileTrainType):
		self.___trainType = aSpeedProfileTrainType

	def __init__(self):
		self.___tilting : SpeedProfileTilting = SpeedProfileTilting.SpeedProfileTilting()
		# @AssociationType Common.SpeedProfileTilting
		# @AssociationMultiplicity 0..1
		self.___load : SpeedProfileLoad = SpeedProfileLoad.SpeedProfileLoad()
		# @AssociationType Common.SpeedProfileLoad
		# @AssociationMultiplicity 0..1
		self.___braking : SpeedProfileBraking = SpeedProfileBraking.SpeedProfileBraking()
		# @AssociationType Common.SpeedProfileBraking
		# @AssociationMultiplicity 0..1
		self.___trainType : SpeedProfileTrainType = SpeedProfileTrainType.SpeedProfileTrainType()
		# @AssociationType Common.SpeedProfileTrainType
		# @AssociationMultiplicity 0..1
		#self._unnamed_aSpeedProfile_ : aSpeedProfile = aSpeedProfile.aSpeedProfile()	#TODO CIRCULAR INCLUDE!

