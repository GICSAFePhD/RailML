#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tBitmaskAny, PeriodRule, TimePeriod
import datetime
from typing import List

class CalendarTimePeriodWithBitmask(TimePeriod.TimePeriod):
	@property
	def FromDate(self) -> datetime:
		return self.___fromDate
	@property
	def Bitmask(self) -> tBitmaskAny:
		return self.___bitmask
	@property
	def PeriodRule(self) -> PeriodRule:
		return self.___periodRule

	@FromDate.setter
	def FromDate(self, aFromDate : datetime):
		self.___fromDate = aFromDate
	@Bitmask.setter
	def Bitmask(self, aBitmask : tBitmaskAny):
		self.___bitmask = aBitmask
	@PeriodRule.setter
	def PeriodRule(self, aPeriodRule : PeriodRule):	# *aPeriodRule
		self.___periodRule = aPeriodRule

	def create_PeriodRule(self):
		if self.PeriodRule == None:
			self.PeriodRule = []
		self.PeriodRule.append(PeriodRule.PeriodRule())

	def __init__(self):
		super().__init__()
		self.___fromDate : datetime = None	#TODO DEFINED AS date
		self.___bitmask : tBitmaskAny = None
		# @AssociationType Common.tBitmaskAny
		self.___periodRule : PeriodRule = None
		# @AssociationType Common.PeriodRule*
		# @AssociationMultiplicity 0..*

