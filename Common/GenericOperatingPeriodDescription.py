#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Common import DateWithBitmask
from Common import PeriodRuleElement
from typing import List

class GenericOperatingPeriodDescription(PeriodRuleElement):
	def setName(self, aName : str):
		self.___name = aName

	def getName(self) -> str:
		return self.___name

	def setIsPublicHoliday(self, aIsPublicHoliday : long):
		self.___isPublicHoliday = aIsPublicHoliday

	def getIsPublicHoliday(self) -> long:
		return self.___isPublicHoliday

	def setDateSet(self, *aDateSet : DateWithBitmask*):
		self._dateSet = aDateSet

	def getDateSet(self) -> DateWithBitmask*:
		return self._dateSet

	def __init__(self):
		self.___name : str = None
		self.___isPublicHoliday : long = None
		self._dateSet : DateWithBitmask = None
		# @AssociationType Common.DateWithBitmask*
		# @AssociationMultiplicity 1..*

