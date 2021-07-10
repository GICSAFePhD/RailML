#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Common import TimePeriodRule
from typing import List

class ShiftablePeriodRule(TimePeriodRule):
	def setShift(self, aShift : integer):
		self.___shift = aShift

	def getShift(self) -> integer:
		return self.___shift

	def __init__(self):
		self.___shift : integer = None

