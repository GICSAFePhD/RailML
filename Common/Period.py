#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common.CalendarTimePeriod import CalendarTimePeriod
from RailML.Common.CalendarTimePeriodWithBitmask import CalendarTimePeriodWithBitmask
from RailML.Common.GenericTimePeriod import GenericTimePeriod
from typing import List

class Period(object):
	def setPeriod(self, aPeriod : CalendarTimePeriod):
		self._period = aPeriod

	def getPeriod(self) -> CalendarTimePeriod:
		return self._period

	def setPeriodBitmask(self, aPeriodBitmask : CalendarTimePeriodWithBitmask):
		self._periodBitmask = aPeriodBitmask

	def getPeriodBitmask(self) -> CalendarTimePeriodWithBitmask:
		return self._periodBitmask

	def setPeriodGeneric(self, aPeriodGeneric : GenericTimePeriod):
		self._periodGeneric = aPeriodGeneric

	def getPeriodGeneric(self) -> GenericTimePeriod:
		return self._periodGeneric

	def __init__(self):
		self._period : CalendarTimePeriod = None
		# @AssociationType Common.CalendarTimePeriod
		# @AssociationMultiplicity 0..1
		self._periodBitmask : CalendarTimePeriodWithBitmask = None
		# @AssociationType Common.CalendarTimePeriodWithBitmask
		# @AssociationMultiplicity 0..1
		self._periodGeneric : GenericTimePeriod = None
		# @AssociationType Common.GenericTimePeriod
		# @AssociationMultiplicity 0..1

