#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import tGroupingTypesExt, EntityIL
from typing import List

class ElementGroupingTypes(EntityIL.EntityIL):
	"""list of possible purposes for element grouping"""
	@property
	def tGroupingTypesExt(self) -> tGroupingTypesExt:
		return self.___elementGroupType
	
	@tGroupingTypesExt.setter
	def tGroupingTypesExt(self, atGroupingTypesExt : tGroupingTypesExt):
		self.___elementGroupType = atGroupingTypesExt

	def __init__(self):
		self.___elementGroupType : tGroupingTypesExt = tGroupingTypesExt.tGroupingTypesExt()
		# @AssociationType Interlocking.tGroupingTypesExt
		# """The classification of the element group."""

