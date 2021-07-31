#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tBitmaskWeek, PeriodRuleElement
from typing import List

class OperatingDay(PeriodRuleElement.PeriodRuleElement):
	@property
	def tBitmaskWeek(self) -> tBitmaskWeek:
		return self.___bitmask
	
	@tBitmaskWeek.setter
	def tBitmaskWeek(self, atBitmaskWeek : tBitmaskWeek):
		self.___bitmask = atBitmaskWeek

	def __init__(self):
		self.___bitmask : tBitmaskWeek = tBitmaskWeek.tBitmaskWeek()
		# @AssociationType Common.tBitmaskWeek

