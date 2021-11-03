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

	def create_SpeedProfileTilting(self):
		self.SpeedProfileTilting = SpeedProfileTilting.SpeedProfileTilting()
	def create_SpeedProfileLoad(self):
		self.SpeedProfileLoad = SpeedProfileLoad.SpeedProfileLoad()
	def create_SpeedProfileBraking(self):
			self.SpeedProfileBraking = SpeedProfileBraking.SpeedProfileBraking()
	def create_SpeedProfileTrainType(self):
			self.SpeedProfileTrainType = SpeedProfileTrainType.SpeedProfileTrainType()

	def __init__(self):
		super().__init__()
		self.___tilting : SpeedProfileTilting = None
		# @AssociationType Common.SpeedProfileTilting
		# @AssociationMultiplicity 0..1
		self.___load : SpeedProfileLoad = None
		# @AssociationType Common.SpeedProfileLoad
		# @AssociationMultiplicity 0..1
		self.___braking : SpeedProfileBraking = None
		# @AssociationType Common.SpeedProfileBraking
		# @AssociationMultiplicity 0..1
		self.___trainType : SpeedProfileTrainType = None
		# @AssociationType Common.SpeedProfileTrainType
		# @AssociationMultiplicity 0..1
		#self._unnamed_aSpeedProfile_ : aSpeedProfile = None	#TODO CIRCULAR INCLUDE!