#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Infrastructure.RTM import RTM_PositioningSystem
from typing import List

class ScreenPositioningSystem(RTM_PositioningSystem):
	def setPxX(self, aPxX : positiveInteger):
		self.___pxX = aPxX

	def getPxX(self) -> positiveInteger:
		return self.___pxX

	def setPxY(self, aPxY : positiveInteger):
		self.___pxY = aPxY

	def getPxY(self) -> positiveInteger:
		return self.___pxY

	def setPxZ(self, aPxZ : positiveInteger):
		self.___pxZ = aPxZ

	def getPxZ(self) -> positiveInteger:
		return self.___pxZ

	def __init__(self):
		self.___pxX : positiveInteger = None
		self.___pxY : positiveInteger = None
		self.___pxZ : positiveInteger = None

