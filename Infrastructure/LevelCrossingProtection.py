#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import tLevelCrossingProtectionBarrierExt, tLevelCrossingProtectionLightsExt,tLevelCrossingProtectionAcousticExt
from typing import List, NewType
Long = NewType("Long", int)

class LevelCrossingProtection(object):
	@property
	def Barriers(self) -> tLevelCrossingProtectionBarrierExt:
		return self.___barriers
	@property
	def Lights(self) -> tLevelCrossingProtectionLightsExt:
		return self.___lights
	@property
	def Acoustic(self) -> tLevelCrossingProtectionAcousticExt:
		return self.___acoustic
	@property
	def HasActiveProtection(self) -> Long:
		return self.___hasActiveProtection

	@Barriers.setter
	def Barriers(self, aBarriers : tLevelCrossingProtectionBarrierExt):
		self.___barriers = aBarriers
	@Lights.setter
	def Lights(self, aLights : tLevelCrossingProtectionLightsExt):
		self.___lights = aLights
	@Acoustic.setter
	def Acoustic(self, aAcoustic : tLevelCrossingProtectionAcousticExt):
		self.___acoustic = aAcoustic
	@HasActiveProtection.setter
	def HasActiveProtection(self, aHasActiveProtection : Long):
		self.___hasActiveProtection = aHasActiveProtection

	def __init__(self):
		self.___barriers : tLevelCrossingProtectionBarrierExt = tLevelCrossingProtectionBarrierExt.tLevelCrossingProtectionBarrierExt()
		# @AssociationType Infrastructure.tLevelCrossingProtectionBarrierExt
		# """technical level crossing protection: barriers;
		# missing attribute means that the information is not known"""
		self.___lights : tLevelCrossingProtectionLightsExt = tLevelCrossingProtectionLightsExt.tLevelCrossingProtectionLightsExt()
		# @AssociationType Infrastructure.tLevelCrossingProtectionLightsExt
		# """technical level crossing protection: lights;
		# missing attribute means that the information is not known"""
		self.___acoustic : tLevelCrossingProtectionAcousticExt = tLevelCrossingProtectionAcousticExt.tLevelCrossingProtectionAcousticExt()
		# @AssociationType Infrastructure.tLevelCrossingProtectionAcousticExt
		# """technical level crossing protection: acoustic warning system;
		# missing attribute means that the information is not known"""
		self.___hasActiveProtection : Long = 0

