#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common.TimePeriodRule import TimePeriodRule
from typing import List

class ShiftablePeriodRule(TimePeriodRule):
	def setShift(self, aShift : int):
		self.___shift = aShift

	def getShift(self) -> int:
		return self.___shift

	def __init__(self):
		self.___shift : int = None

