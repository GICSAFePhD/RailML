#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import PeriodRule, PublicHolidayPeriodRule, ElemBasedPeriodRule
import datetime
from typing import List

class TimePeriodRuleSituation(object):
	@property
	def FromDate(self) -> datetime:
		return self.___fromDate
	@property
	def PeriodRule(self) -> PeriodRule:
		return self.___periodRule
	@property
	def PublicHolidayPeriodRule(self) -> PublicHolidayPeriodRule:
		return self.___publicHolidayPeriodRule
	@property
	def ElementBasedPeriodRule(self) -> ElemBasedPeriodRule:
		return self.___elementBasedPeriodRule

	@FromDate.setter
	def FromDate(self, aFromDate : datetime):
		self.___fromDate = aFromDate
	@PeriodRule.setter
	def PeriodRule(self, aPeriodRule : PeriodRule):
		self.___periodRule = aPeriodRule
	@PublicHolidayPeriodRule.setter
	def PublicHolidayPeriodRule(self, aPublicHolidayPeriodRule : PublicHolidayPeriodRule):
		self.___publicHolidayPeriodRule = aPublicHolidayPeriodRule
	@ElementBasedPeriodRule.setter
	def ElementBasedPeriodRule(self, aElementBasedPeriodRule : ElemBasedPeriodRule):
		self.___elementBasedPeriodRule = aElementBasedPeriodRule

	def __init__(self):
		self.___fromDate : datetime = 0	#TODO DEFINED AS date
		self.___periodRule : PeriodRule = PeriodRule.PeriodRule()
		# @AssociationType Common.PeriodRule
		# @AssociationMultiplicity 0..1
		self.___publicHolidayPeriodRule : PublicHolidayPeriodRule = PublicHolidayPeriodRule.PublicHolidayPeriodRule()
		# @AssociationType Common.PublicHolidayPeriodRule
		# @AssociationMultiplicity 0..1
		self.___elementBasedPeriodRule : ElemBasedPeriodRule = ElemBasedPeriodRule.ElemBasedPeriodRule()
		# @AssociationType Common.ElemBasedPeriodRule
		# @AssociationMultiplicity 0..1

