#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tSpeedProfileInfluence, SpeedProfile
from typing import List

class aSpeedProfile(object):
	@property
	def tSpeedProfileInfluence(self) -> tSpeedProfileInfluence:
		return self.___influence
	@property
	def SpeedProfile(self) -> SpeedProfile:
		return self.___unnamed_SpeedProfile_

	@tSpeedProfileInfluence.setter
	def tSpeedProfileInfluence(self, atSpeedProfileInfluence : tSpeedProfileInfluence):
		self.___influence = atSpeedProfileInfluence
	@SpeedProfile.setter
	def SpeedProfile(self, aSpeedProfile : SpeedProfile):
		self.___unnamed_SpeedProfile_ = aSpeedProfile

	def __init__(self):
		self.___influence : tSpeedProfileInfluence = tSpeedProfileInfluence.tSpeedProfileInfluence()
		# @AssociationType Common.tSpeedProfileInfluence
		self.___unnamed_SpeedProfile_ : SpeedProfile = SpeedProfile.SpeedProfile()

