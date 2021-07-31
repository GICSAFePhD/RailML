#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import DateWithBitmask, PeriodRuleElement
from typing import List, NewType
Long = NewType("Long", int)

class GenericOperatingPeriodDescription(PeriodRuleElement.PeriodRuleElement):
	@property
	def Name(self) -> str:
		return self.___name
	@property
	def IsPublicHoliday(self) -> Long:
		return self.___isPublicHoliday
	@property
	def DateSet(self) -> DateWithBitmask:
		return self.___dateSet

	@Name.setter
	def Name(self, aName : str):
		self.___name = aName
	@IsPublicHoliday.setter
	def IsPublicHoliday(self, aIsPublicHoliday : Long):
		self.___isPublicHoliday = aIsPublicHoliday
	@DateSet.setter
	def DateSet(self, *aDateSet : DateWithBitmask):
		self.___dateSet = aDateSet

	def __init__(self):
		self.___name : str = ""
		self.___isPublicHoliday : Long = 0
		self.___dateSet : DateWithBitmask = DateWithBitmask.DateWithBitmask()
		# @AssociationType Common.DateWithBitmask*
		# @AssociationMultiplicity 1..*

