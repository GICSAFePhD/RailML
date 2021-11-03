#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.RailTopoModel import RTM_PositioningSystem
from typing import List, NewType

PositiveInteger = NewType("PositiveInteger", int)	#TODO EVERY INT SHOULD BE A POSITIVEINTEGER

class ScreenPositioningSystem(RTM_PositioningSystem.RTM_PositioningSystem):
	@property
	def pxX(self) -> PositiveInteger:
		return self.___pxX
	@property
	def pxY(self) -> PositiveInteger:
		return self.___pxY
	@property
	def pxZ(self) -> PositiveInteger:
		return self.___pxZ

	@pxX.setter
	def pxX(self, apxX : PositiveInteger):
		self.___pxX = apxX
	@pxY.setter
	def pxY(self, apxY : PositiveInteger):
		self.___pxY = apxY
	@pxZ.setter
	def pxZ(self, apxZ : PositiveInteger):
		self.___pxZ = apxZ

	def __init__(self):
		super().__init__()
		self.___pxX : PositiveInteger = None
		self.___pxY : PositiveInteger = None
		self.___pxZ : PositiveInteger = None