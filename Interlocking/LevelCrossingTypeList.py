#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Interlocking import tLevelCrossingControlTypes
from Interlocking import EntityIL
from typing import List

class LevelCrossingTypeList(EntityIL):
	"""The level crossings have some basic features which can be specified independent of the particular manufacturer. Most important is the control type saying how the control relation between the interlocking and the level crossing is."""
	def setControlType(self, aControlType : tLevelCrossingControlTypes):
		self.___controlType = aControlType

	def getControlType(self) -> tLevelCrossingControlTypes:
		return self.___controlType

	def setAllowsLocalOperation(self, aAllowsLocalOperation : long):
		self.___allowsLocalOperation = aAllowsLocalOperation

	def getAllowsLocalOperation(self) -> long:
		return self.___allowsLocalOperation

	def setHasBarrier(self, aHasBarrier : long):
		self.___hasBarrier = aHasBarrier

	def getHasBarrier(self) -> long:
		return self.___hasBarrier

	def setHasTrafficWarning(self, aHasTrafficWarning : long):
		self.___hasTrafficWarning = aHasTrafficWarning

	def getHasTrafficWarning(self) -> long:
		return self.___hasTrafficWarning

	def __init__(self):
		self.___controlType : tLevelCrossingControlTypes = None
		# @AssociationType Interlocking.tLevelCrossingControlTypes
		# """The classification of the control type w.r.t. the interlocking operation."""
		self.___allowsLocalOperation : long = None
		"""The level crossing may have a control unit which allows local operation from the field."""
		self.___hasBarrier : long = None
		"""The level crossing may be equipped with barriers for road traffic."""
		self.___hasTrafficWarning : long = None
		"""The level crossing may be equipped with audible/optical means to allow warning of road traffic."""

