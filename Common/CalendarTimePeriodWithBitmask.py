#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common.tBitmaskAny import tBitmaskAny
from RailML.Common.PeriodRule import PeriodRule
from RailML.Common.TimePeriod import TimePeriod
import datetime
from typing import List

class CalendarTimePeriodWithBitmask(TimePeriod):
	def setFromDate(self, aFromDate : datetime):	#TODO DEFINED AS date
		self.___fromDate = aFromDate

	def getFromDate(self) -> datetime:	#TODO DEFINED AS date
		return self.___fromDate

	def setBitmask(self, aBitmask : tBitmaskAny):
		self.___bitmask = aBitmask

	def getBitmask(self) -> tBitmaskAny:
		return self.___bitmask

	def setPeriodRule(self, *aPeriodRule : PeriodRule):
		self._periodRule = aPeriodRule

	def getPeriodRule(self) -> PeriodRule:
		return self._periodRule

	def __init__(self):
		self.___fromDate : datetime = None	#TODO DEFINED AS date
		self.___bitmask : tBitmaskAny = None
		# @AssociationType Common.tBitmaskAny
		self._periodRule : PeriodRule = None
		# @AssociationType Common.PeriodRule*
		# @AssociationMultiplicity 0..*

