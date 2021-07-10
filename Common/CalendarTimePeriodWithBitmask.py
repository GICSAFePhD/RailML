#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Common import tBitmaskAny
from Common import PeriodRule
from Common import TimePeriod
from typing import List

class CalendarTimePeriodWithBitmask(TimePeriod):
	def setFromDate(self, aFromDate : date):
		self.___fromDate = aFromDate

	def getFromDate(self) -> date:
		return self.___fromDate

	def setBitmask(self, aBitmask : tBitmaskAny):
		self.___bitmask = aBitmask

	def getBitmask(self) -> tBitmaskAny:
		return self.___bitmask

	def setPeriodRule(self, *aPeriodRule : PeriodRule*):
		self._periodRule = aPeriodRule

	def getPeriodRule(self) -> PeriodRule*:
		return self._periodRule

	def __init__(self):
		self.___fromDate : date = None
		self.___bitmask : tBitmaskAny = None
		# @AssociationType Common.tBitmaskAny
		self._periodRule : PeriodRule = None
		# @AssociationType Common.PeriodRule*
		# @AssociationMultiplicity 0..*

