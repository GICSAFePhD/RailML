#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Infrastructure import tLevelCrossingProtectionBarrierExt
from Infrastructure import tLevelCrossingProtectionLightsExt
from Infrastructure import tLevelCrossingProtectionAcousticExt
from typing import List

class LevelCrossingProtection(object):
	def setBarriers(self, aBarriers : tLevelCrossingProtectionBarrierExt):
		self.___barriers = aBarriers

	def getBarriers(self) -> tLevelCrossingProtectionBarrierExt:
		return self.___barriers

	def setLights(self, aLights : tLevelCrossingProtectionLightsExt):
		self.___lights = aLights

	def getLights(self) -> tLevelCrossingProtectionLightsExt:
		return self.___lights

	def setAcoustic(self, aAcoustic : tLevelCrossingProtectionAcousticExt):
		self.___acoustic = aAcoustic

	def getAcoustic(self) -> tLevelCrossingProtectionAcousticExt:
		return self.___acoustic

	def setHasActiveProtection(self, aHasActiveProtection : long):
		self.___hasActiveProtection = aHasActiveProtection

	def getHasActiveProtection(self) -> long:
		return self.___hasActiveProtection

	def __init__(self):
		self.___barriers : tLevelCrossingProtectionBarrierExt = None
		# @AssociationType Infrastructure.tLevelCrossingProtectionBarrierExt
		# """technical level crossing protection: barriers;
		# missing attribute means that the information is not known"""
		self.___lights : tLevelCrossingProtectionLightsExt = None
		# @AssociationType Infrastructure.tLevelCrossingProtectionLightsExt
		# """technical level crossing protection: lights;
		# missing attribute means that the information is not known"""
		self.___acoustic : tLevelCrossingProtectionAcousticExt = None
		# @AssociationType Infrastructure.tLevelCrossingProtectionAcousticExt
		# """technical level crossing protection: acoustic warning system;
		# missing attribute means that the information is not known"""
		self.___hasActiveProtection : long = None

