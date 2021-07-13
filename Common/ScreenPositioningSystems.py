#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common.ScreenPositioningSystem import ScreenPositioningSystem
from typing import List

class ScreenPositioningSystems(object):
	def setScreenPositioningSystem(self, aScreenPositioningSystem : ScreenPositioningSystem):
		self._screenPositioningSystem = aScreenPositioningSystem

	def getScreenPositioningSystem(self) -> ScreenPositioningSystem:
		return self._screenPositioningSystem

	def __init__(self):
		self._screenPositioningSystem : ScreenPositioningSystem = None
		# @AssociationType Common.ScreenPositioningSystem*
		# @AssociationMultiplicity 1..*

