#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import CalendarTimePeriod, CalendarTimePeriodWithBitmask, GenericTimePeriod
from typing import List

class Period(object):
	@property
	def Period(self) -> CalendarTimePeriod:
		return self.___period
	@property
	def PeriodBitmask(self) -> CalendarTimePeriodWithBitmask:
		return self.___periodBitmask
	@property
	def PeriodGeneric(self) -> GenericTimePeriod:
		return self.___periodGeneric

	@Period.setter
	def Period(self, aPeriod : CalendarTimePeriod):
		self.___period = aPeriod
	@PeriodBitmask.setter
	def PeriodBitmask(self, aPeriodBitmask : CalendarTimePeriodWithBitmask):
		self.___periodBitmask = aPeriodBitmask
	@PeriodGeneric.setter
	def PeriodGeneric(self, aPeriodGeneric : GenericTimePeriod):
		self.___periodGeneric = aPeriodGeneric

	def create_Period(self):
		if self.Period == None:
			self.Period = []
		self.Period.append(CalendarTimePeriod.CalendarTimePeriod())
	def create_PeriodBitmask(self):
		if self.PeriodBitmask == None:
			self.PeriodBitmask = []
		self.PeriodBitmask.append(CalendarTimePeriodWithBitmask.CalendarTimePeriodWithBitmask())
	def create_PeriodGeneric(self):
		if self.PeriodGeneric == None:
			self.PeriodGeneric = []
		self.PeriodGeneric.append(GenericTimePeriod.GenericTimePeriod())

	def __init__(self):
		self.___period : CalendarTimePeriod = None
		# @AssociationType Common.CalendarTimePeriod
		# @AssociationMultiplicity 0..1
		self.___periodBitmask : CalendarTimePeriodWithBitmask = None
		# @AssociationType Common.CalendarTimePeriodWithBitmask
		# @AssociationMultiplicity 0..1
		self.___periodGeneric : GenericTimePeriod = None
		# @AssociationType Common.GenericTimePeriod
		# @AssociationMultiplicity 0..1