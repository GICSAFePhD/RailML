#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import CalendarTimePeriod, CalendarTimePeriodWithBitmask, GenericTimePeriod
from typing import List

class Period(object):
	@property
	def CalendarTimePeriod(self) -> CalendarTimePeriod:
		return self.___period
	@property
	def CalendarTimePeriodWithBitmask(self) -> CalendarTimePeriodWithBitmask:
		return self.___periodBitmask
	@property
	def GenericTimePeriod(self) -> GenericTimePeriod:
		return self.___periodGeneric

	@CalendarTimePeriod.setter
	def CalendarTimePeriod(self, aCalendarTimePeriod : CalendarTimePeriod):
		self.___period = aCalendarTimePeriod
	@CalendarTimePeriodWithBitmask.setter
	def CalendarTimePeriodWithBitmask(self, aCalendarTimePeriodWithBitmask : CalendarTimePeriodWithBitmask):
		self.___periodBitmask = aCalendarTimePeriodWithBitmask
	@GenericTimePeriod.setter
	def GenericTimePeriod(self, aGenericTimePeriod : GenericTimePeriod):
		self.___periodGeneric = aGenericTimePeriod

	def __init__(self):
		self.___period : CalendarTimePeriod = CalendarTimePeriod.CalendarTimePeriod()
		# @AssociationType Common.CalendarTimePeriod
		# @AssociationMultiplicity 0..1
		self.___periodBitmask : CalendarTimePeriodWithBitmask = CalendarTimePeriodWithBitmask.CalendarTimePeriodWithBitmask()
		# @AssociationType Common.CalendarTimePeriodWithBitmask
		# @AssociationMultiplicity 0..1
		self.___periodGeneric : GenericTimePeriod = GenericTimePeriod.GenericTimePeriod()
		# @AssociationType Common.GenericTimePeriod
		# @AssociationMultiplicity 0..1

