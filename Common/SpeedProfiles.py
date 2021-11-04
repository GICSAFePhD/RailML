#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import SpeedProfile
from typing import List

class SpeedProfiles(object):
	@property
	def SpeedProfile(self) -> SpeedProfile:
		return self.___speedProfile

	@SpeedProfile.setter
	def SpeedProfile(self, aSpeedProfile : SpeedProfile):
		self.___speedProfile = aSpeedProfile

	def create_SpeedProfile(self):
		if self.SpeedProfile == None:
			self.SpeedProfile = []
		self.SpeedProfile.append(SpeedProfile.SpeedProfile())

	def __init__(self):
		self.___speedProfile : SpeedProfile = None
		# @AssociationType Common.SpeedProfile*
		# @AssociationMultiplicity 1..*