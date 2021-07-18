#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking.tLevelCrossingControlTypes import tLevelCrossingControlTypes
from RailML.Interlocking.EntityIL import EntityIL
from typing import List

class LevelCrossingTypeList(EntityIL):
	"""The level crossings have some basic features which can be specified independent of the particular manufacturer. Most important is the control type saying how the control relation between the interlocking and the level crossing is."""
	def setControlType(self, aControlType : tLevelCrossingControlTypes):
		self.___controlType = aControlType

	def getControlType(self) -> tLevelCrossingControlTypes:
		return self.___controlType

	def setAllowsLocalOperation(self, aAllowsLocalOperation : int):	#TODO DEFINED AS LONG
		self.___allowsLocalOperation = aAllowsLocalOperation

	def getAllowsLocalOperation(self) -> int:	#TODO DEFINED AS LONG
		return self.___allowsLocalOperation

	def setHasBarrier(self, aHasBarrier : int):	#TODO DEFINED AS LONG
		self.___hasBarrier = aHasBarrier

	def getHasBarrier(self) -> int:	#TODO DEFINED AS LONG
		return self.___hasBarrier

	def setHasTrafficWarning(self, aHasTrafficWarning : int):	#TODO DEFINED AS LONG
		self.___hasTrafficWarning = aHasTrafficWarning

	def getHasTrafficWarning(self) -> int:	#TODO DEFINED AS LONG
		return self.___hasTrafficWarning

	def __init__(self):
		self.___controlType : tLevelCrossingControlTypes = None
		# @AssociationType Interlocking.tLevelCrossingControlTypes
		# """The classification of the control type w.r.t. the interlocking operation."""
		self.___allowsLocalOperation : int = None	#TODO DEFINED AS LONG
		"""The level crossing may have a control unit which allows local operation from the field."""
		self.___hasBarrier : int = None	#TODO DEFINED AS LONG
		"""The level crossing may be equipped with barriers for road traffic."""
		self.___hasTrafficWarning : int = None	#TODO DEFINED AS LONG
		"""The level crossing may be equipped with audible/optical means to allow warning of road traffic."""

