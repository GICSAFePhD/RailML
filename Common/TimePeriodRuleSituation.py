#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Common import PeriodRule
from Common import PublicHolidayPeriodRule
from Common import ElemBasedPeriodRule
from typing import List

class TimePeriodRuleSituation(object):
	def setFromDate(self, aFromDate : date):
		self.___fromDate = aFromDate

	def getFromDate(self) -> date:
		return self.___fromDate

	def setPeriodRule(self, aPeriodRule : PeriodRule):
		self._periodRule = aPeriodRule

	def getPeriodRule(self) -> PeriodRule:
		return self._periodRule

	def setPublicHolidayPeriodRule(self, aPublicHolidayPeriodRule : PublicHolidayPeriodRule):
		self._publicHolidayPeriodRule = aPublicHolidayPeriodRule

	def getPublicHolidayPeriodRule(self) -> PublicHolidayPeriodRule:
		return self._publicHolidayPeriodRule

	def setElementBasedPeriodRule(self, aElementBasedPeriodRule : ElemBasedPeriodRule):
		self._elementBasedPeriodRule = aElementBasedPeriodRule

	def getElementBasedPeriodRule(self) -> ElemBasedPeriodRule:
		return self._elementBasedPeriodRule

	def __init__(self):
		self.___fromDate : date = None
		self._periodRule : PeriodRule = None
		# @AssociationType Common.PeriodRule
		# @AssociationMultiplicity 0..1
		self._publicHolidayPeriodRule : PublicHolidayPeriodRule = None
		# @AssociationType Common.PublicHolidayPeriodRule
		# @AssociationMultiplicity 0..1
		self._elementBasedPeriodRule : ElemBasedPeriodRule = None
		# @AssociationType Common.ElemBasedPeriodRule
		# @AssociationMultiplicity 0..1

