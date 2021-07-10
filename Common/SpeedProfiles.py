#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Common import SpeedProfile
from typing import List

class SpeedProfiles(object):
	def setSpeedProfile(self, *aSpeedProfile : SpeedProfile*):
		self._speedProfile = aSpeedProfile

	def getSpeedProfile(self) -> SpeedProfile*:
		return self._speedProfile

	def __init__(self):
		self._speedProfile : SpeedProfile = None
		# @AssociationType Common.SpeedProfile*
		# @AssociationMultiplicity 1..*

