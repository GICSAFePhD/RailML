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

	def __init__(self):
		self.___screenPositioningSystem : ScreenPositioningSystem = ScreenPositioningSystem.ScreenPositioningSystem()
		# @AssociationType Common.ScreenPositioningSystem*
		# @AssociationMultiplicity 1..*

