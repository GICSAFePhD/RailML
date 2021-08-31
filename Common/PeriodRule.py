#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import ClockTimePeriod, TimePeriodRule
from typing import List

class PeriodRule(TimePeriodRule.TimePeriodRule):
	@property
	def Period(self) -> ClockTimePeriod:
		return self.___period
	
	@Period.setter
	def Period(self, aPeriod : ClockTimePeriod): # TODO *aPeriod
		self.___period = aPeriod

	def create_Period(self):
		if self.Period == None:
			self.Period = []
		self.Period.append(ClockTimePeriod.ClockTimePeriod())

	def __init__(self):
		self.___period : ClockTimePeriod = None
		# @AssociationType Common.ClockTimePeriod*
		# @AssociationMultiplicity 1..*

