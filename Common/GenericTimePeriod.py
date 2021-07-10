#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Common import TimePeriodRuleSituation
from Common import TimePeriod
from typing import List

class GenericTimePeriod(TimePeriod):
	def setContainedSituation(self, *aContainedSituation : TimePeriodRuleSituation*):
		self._containedSituation = aContainedSituation

	def getContainedSituation(self) -> TimePeriodRuleSituation*:
		return self._containedSituation

	def __init__(self):
		self._containedSituation : TimePeriodRuleSituation = None
		# @AssociationType Common.TimePeriodRuleSituation*
		# @AssociationMultiplicity 1..*

