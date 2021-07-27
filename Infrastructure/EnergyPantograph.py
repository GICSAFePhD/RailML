#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import tTSIPantoHeadTypeList, tPantoHeadTypeList, tContactStripMaterialList
from typing import List, NewType

Long = NewType("Long", int)

class EnergyPantograph(object):
	@property
	def RequiresTSIcompliance(self) -> Long:
		return self.___requiresTSIcompliance
	@property
	def tTSIPantoHeadTypeList(self) -> tTSIPantoHeadTypeList:
		return self.___compliantTSITypes
	@property
	def tPantoHeadTypeList(self) -> tPantoHeadTypeList:
		return self.___nationalPanHeadTypes
	@property
	def tContactStripMaterialList(self) -> tContactStripMaterialList:
		return self.___contactStripMaterials

	@RequiresTSIcompliance.setter
	def RequiresTSIcompliance(self, aRequiresTSIcompliance : Long):
		self.___requiresTSIcompliance = aRequiresTSIcompliance
	@tTSIPantoHeadTypeList.setter
	def tTSIPantoHeadTypeList(self, atTSIPantoHeadTypeList : tTSIPantoHeadTypeList):
		self.___compliantTSITypes = atTSIPantoHeadTypeList
	@tPantoHeadTypeList.setter
	def tPantoHeadTypeList(self, atPantoHeadTypeList : tPantoHeadTypeList):
		self.___nationalPanHeadTypes = atPantoHeadTypeList
	@tContactStripMaterialList.setter
	def tContactStripMaterialList(self, atContactStripMaterialList : tContactStripMaterialList):
		self.___contactStripMaterials = atContactStripMaterialList
  
	def __init__(self):
		self.___requiresTSIcompliance : Long = 0
		"""flag, whether a TSI complaint pantograph head is required"""
		self.___compliantTSITypes : tTSIPantoHeadTypeList = tTSIPantoHeadTypeList.tTSIPantoHeadTypeList()
		# @AssociationType Infrastructure.tTSIPantoHeadTypeList
		# """space separated list of accepted TSI compliant pantograph heads"""
		self.___nationalPanHeadTypes : tPantoHeadTypeList = tPantoHeadTypeList.tPantoHeadTypeList()
		# @AssociationType Infrastructure.tPantoHeadTypeList
		# """space separated list of accepted other pantograph heads"""
		self.___contactStripMaterials : tContactStripMaterialList = tContactStripMaterialList.tContactStripMaterialList()
		# @AssociationType Infrastructure.tContactStripMaterialList
		# """space separated list of permitted contact strip materials"""

