#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure.RTM_PositioningSystem import RTM_PositioningSystem
from typing import List

#TODO EVERY INT SHOULD BE A POSITIVEINTEGER

class ScreenPositioningSystem(RTM_PositioningSystem):
	def setPxX(self, aPxX : int):
		self.___pxX = aPxX

	def getPxX(self) -> int:
		return self.___pxX

	def setPxY(self, aPxY : int):
		self.___pxY = aPxY

	def getPxY(self) -> int:
		return self.___pxY

	def setPxZ(self, aPxZ : int):
		self.___pxZ = aPxZ

	def getPxZ(self) -> int:
		return self.___pxZ

	def __init__(self):
		self.___pxX : int = None
		self.___pxY : int = None
		self.___pxZ : int = None

