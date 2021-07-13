#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common.tSpeedProfileInfluence import tSpeedProfileInfluence
from RailML.Common.SpeedProfile import SpeedProfile
from typing import List

class aSpeedProfile(object):
	def setInfluence(self, aInfluence : tSpeedProfileInfluence):
		self.___influence = aInfluence

	def getInfluence(self) -> tSpeedProfileInfluence:
		return self.___influence

	def __init__(self):
		self.___influence : tSpeedProfileInfluence = None
		# @AssociationType Common.tSpeedProfileInfluence
		self._unnamed_SpeedProfile_ : SpeedProfile = None

