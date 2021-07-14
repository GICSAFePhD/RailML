#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure.tTSIPantoHeadTypeList import tTSIPantoHeadTypeList
from RailML.Infrastructure.tPantoHeadTypeList import tPantoHeadTypeList
from RailML.Infrastructure.tContactStripMaterialList import tContactStripMaterialList
from typing import List

class EnergyPantograph(object):
	def setRequiresTSIcompliance(self, aRequiresTSIcompliance : int): #TODO DEFINED AS LONG
		self.___requiresTSIcompliance = aRequiresTSIcompliance

	def getRequiresTSIcompliance(self) -> int:	 #TODO DEFINED AS LONG
		return self.___requiresTSIcompliance

	def setCompliantTSITypes(self, aCompliantTSITypes : tTSIPantoHeadTypeList):
		self.___compliantTSITypes = aCompliantTSITypes

	def getCompliantTSITypes(self) -> tTSIPantoHeadTypeList:
		return self.___compliantTSITypes

	def setNationalPanHeadTypes(self, aNationalPanHeadTypes : tPantoHeadTypeList):
		self.___nationalPanHeadTypes = aNationalPanHeadTypes

	def getNationalPanHeadTypes(self) -> tPantoHeadTypeList:
		return self.___nationalPanHeadTypes

	def setContactStripMaterials(self, aContactStripMaterials : tContactStripMaterialList):
		self.___contactStripMaterials = aContactStripMaterials

	def getContactStripMaterials(self) -> tContactStripMaterialList:
		return self.___contactStripMaterials

	def __init__(self):
		self.___requiresTSIcompliance : int = None #TODO DEFINED AS LONG
		"""flag, whether a TSI complaint pantograph head is required"""
		self.___compliantTSITypes : tTSIPantoHeadTypeList = None
		# @AssociationType Infrastructure.tTSIPantoHeadTypeList
		# """space separated list of accepted TSI compliant pantograph heads"""
		self.___nationalPanHeadTypes : tPantoHeadTypeList = None
		# @AssociationType Infrastructure.tPantoHeadTypeList
		# """space separated list of accepted other pantograph heads"""
		self.___contactStripMaterials : tContactStripMaterialList = None
		# @AssociationType Infrastructure.tContactStripMaterialList
		# """space separated list of permitted contact strip materials"""

