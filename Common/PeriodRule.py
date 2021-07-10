#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Common import ClockTimePeriod
from Common import TimePeriodRule
from typing import List

class PeriodRule(TimePeriodRule):
	def setPeriod(self, *aPeriod : ClockTimePeriod*):
		self._period = aPeriod

	def getPeriod(self) -> ClockTimePeriod*:
		return self._period

	def __init__(self):
		self._period : ClockTimePeriod = None
		# @AssociationType Common.ClockTimePeriod*
		# @AssociationMultiplicity 1..*

