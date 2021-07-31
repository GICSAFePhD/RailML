#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import ClockTimePeriod, TimePeriodRule
from typing import List

class PeriodRule(TimePeriodRule.TimePeriodRule):
	@property
	def Period(self) -> ClockTimePeriod:
		return self.___period
	
	@Period.setter
	def Period(self, *aPeriod : ClockTimePeriod):
		self.___period = aPeriod

	def __init__(self):
		self.___period : ClockTimePeriod = ClockTimePeriod.ClockTimePeriod()
		# @AssociationType Common.ClockTimePeriod*
		# @AssociationMultiplicity 1..*

