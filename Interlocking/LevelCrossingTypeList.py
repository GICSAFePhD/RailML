#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import tLevelCrossingControlTypes, EntityIL
from typing import List, NewType
Long = NewType("Long", int)

class LevelCrossingTypeList(EntityIL.EntityIL):
	"""The level crossings have some basic features which can be specified independent of the particular manufacturer. Most important is the control type saying how the control relation between the interlocking and the level crossing is."""
	@property
	def ControlType(self) -> tLevelCrossingControlTypes:
		return self.___controlType
	@property
	def AllowsLocalOperation(self) -> Long:
		return self.___allowsLocalOperation
	@property
	def HasBarrier(self) -> Long:
		return self.___hasBarrier
	@property
	def HasTrafficWarning(self) -> Long:
		return self.___hasTrafficWarning

	@ControlType.setter
	def ControlType(self, aControlType : tLevelCrossingControlTypes):
		self.___controlType = aControlType
	@AllowsLocalOperation.setter
	def AllowsLocalOperation(self, aAllowsLocalOperation : Long):
		self.___allowsLocalOperation = aAllowsLocalOperation
	@HasBarrier.setter
	def HasBarrier(self, aHasBarrier : Long):
		self.___hasBarrier = aHasBarrier
	@HasTrafficWarning.setter
	def HasTrafficWarning(self, aHasTrafficWarning : Long):
		self.___hasTrafficWarning = aHasTrafficWarning

	def __init__(self):
		super().__init__()
		self.___controlType : tLevelCrossingControlTypes = None
		# @AssociationType Interlocking.tLevelCrossingControlTypes
		# """The classification of the control type w.r.t. the interlocking operation."""
		self.___allowsLocalOperation : Long = None
		"""The level crossing may have a control unit which allows local operation from the field."""
		self.___hasBarrier : Long = None
		"""The level crossing may be equipped with barriers for road traffic."""
		self.___hasTrafficWarning :Long = None
		"""The level crossing may be equipped with audible/optical means to allow warning of road traffic."""

