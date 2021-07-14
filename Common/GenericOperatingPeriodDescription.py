#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common.DateWithBitmask import DateWithBitmask
from RailML.Common.PeriodRuleElement import PeriodRuleElement
from typing import List

class GenericOperatingPeriodDescription(PeriodRuleElement):
	def setName(self, aName : str):
		self.___name = aName

	def getName(self) -> str:
		return self.___name

	def setIsPublicHoliday(self, aIsPublicHoliday : int):	#TODO DEFINED AS LONG
		self.___isPublicHoliday = aIsPublicHoliday

	def getIsPublicHoliday(self) -> int:	#TODO DEFINED AS LONG
		return self.___isPublicHoliday

	def setDateSet(self, *aDateSet : DateWithBitmask):	#TODO DEFINED AS LONG
		self._dateSet = aDateSet

	def getDateSet(self) -> DateWithBitmask:
		return self._dateSet

	def __init__(self):
		self.___name : str = None
		self.___isPublicHoliday : int = None	#TODO DEFINED AS LONG
		self._dateSet : DateWithBitmask = None
		# @AssociationType Common.DateWithBitmask*
		# @AssociationMultiplicity 1..*

