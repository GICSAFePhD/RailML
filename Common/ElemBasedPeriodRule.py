#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common.OperatingDay import OperatingDay
from RailML.Common.GenericOperatingPeriodDescription import GenericOperatingPeriodDescription
from RailML.Common.ShiftablePeriodRule import ShiftablePeriodRule
from typing import List

class ElemBasedPeriodRule(ShiftablePeriodRule):
	def setOperatingDay(self, aOperatingDay : OperatingDay):
		self._operatingDay = aOperatingDay

	def getOperatingDay(self) -> OperatingDay:
		return self._operatingDay

	def setGenericOperatingPeriod(self, aGenericOperatingPeriod : GenericOperatingPeriodDescription):
		self._genericOperatingPeriod = aGenericOperatingPeriod

	def getGenericOperatingPeriod(self) -> GenericOperatingPeriodDescription:
		return self._genericOperatingPeriod

	def __init__(self):
		self._operatingDay : OperatingDay = None
		# @AssociationType Common.OperatingDay
		# @AssociationMultiplicity 0..1
		self._genericOperatingPeriod : GenericOperatingPeriodDescription = None
		# @AssociationType Common.GenericOperatingPeriodDescription
		# @AssociationMultiplicity 0..1

