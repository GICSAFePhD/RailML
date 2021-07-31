#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import TimePeriodRuleSituation,TimePeriod
from typing import List

class GenericTimePeriod(TimePeriod.TimePeriod):
	@property
	def ContainedSituation(self) -> TimePeriodRuleSituation:
		return self.___containedSituation
	
	@ContainedSituation.setter
	def ContainedSituation(self, *aTimePeriodRuleSituation : TimePeriodRuleSituation):
		self.___containedSituation = aTimePeriodRuleSituation

	def __init__(self):
		self.___containedSituation : TimePeriodRuleSituation = TimePeriodRuleSituation.TimePeriodRuleSituation()
		# @AssociationType Common.TimePeriodRuleSituation*
		# @AssociationMultiplicity 1..*

