#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking.tGroupingTypesExt import tGroupingTypesExt
from RailML.Interlocking.EntityIL import EntityIL
from typing import List

class ElementGroupingTypes(EntityIL):
	"""list of possible purposes for element grouping"""
	def setElementGroupType(self, aElementGroupType : tGroupingTypesExt):
		self.___elementGroupType = aElementGroupType

	def getElementGroupType(self) -> tGroupingTypesExt:
		return self.___elementGroupType

	def __init__(self):
		self.___elementGroupType : tGroupingTypesExt = None
		# @AssociationType Interlocking.tGroupingTypesExt
		# """The classification of the element group."""

