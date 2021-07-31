#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import OperatingDay, GenericOperatingPeriodDescription, ShiftablePeriodRule
from typing import List

class ElemBasedPeriodRule(ShiftablePeriodRule.ShiftablePeriodRule):
	@property
	def OperatingDay(self) -> OperatingDay:
		return self.___operatingDay
	@property
	def GenericOperatingPeriodDescription(self) -> GenericOperatingPeriodDescription:
		return self.___genericOperatingPeriod

	@OperatingDay.setter
	def OperatingDay(self, aOperatingDay : OperatingDay):
		self.___operatingDay = aOperatingDay
	@GenericOperatingPeriodDescription.setter
	def GenericOperatingPeriodDescription(self, aGenericOperatingPeriodDescription : GenericOperatingPeriodDescription):
		self.___genericOperatingPeriod = aGenericOperatingPeriodDescription

	def __init__(self):
		self.___operatingDay : OperatingDay = OperatingDay.OperatingDay()
		# @AssociationType Common.OperatingDay
		# @AssociationMultiplicity 0..1
		self.___genericOperatingPeriod : GenericOperatingPeriodDescription = GenericOperatingPeriodDescription.GenericOperatingPeriodDescription()
		# @AssociationType Common.GenericOperatingPeriodDescription
		# @AssociationMultiplicity 0..1

