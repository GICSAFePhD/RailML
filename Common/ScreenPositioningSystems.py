#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import ScreenPositioningSystem
from typing import List

class ScreenPositioningSystems(object):
	@property
	def ScreenPositioningSystem(self) -> ScreenPositioningSystem:
		return self.___screenPositioningSystem
	
	@ScreenPositioningSystem.setter
	def ScreenPositioningSystem(self, aScreenPositioningSystem : ScreenPositioningSystem):
		self.___screenPositioningSystem = aScreenPositioningSystem

	def create_ScreenPositioningSystem(self):
		if self.ScreenPositioningSystem == None:
			self.ScreenPositioningSystem = []
		self.ScreenPositioningSystem.append(ScreenPositioningSystem.ScreenPositioningSystem())

	def __init__(self):
		self.___screenPositioningSystem : ScreenPositioningSystem = None # It should be [ScreenPositioningSystem.ScreenPositioningSystem()] but it is better to behave as it was a 0..*
		# @AssociationType Common.ScreenPositioningSystem*
		# @AssociationMultiplicity 1..*
		# Everytime <screenPositioningSystems> appears then a <screenPositioningSystem> exists, the 1..* is achieved even without the CORRECT definition

