#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import TimePeriod
import time
from typing import List

class ClockTimePeriod(TimePeriod.TimePeriod):
	@property
	def From_62(self) -> time:
		return self.___from_62
	@property
	def To(self) -> time:
		return self.___to

	@From_62.setter
	def From_62(self, aFrom_62 : time):
		self.___from_62 = aFrom_62
	@To.setter
	def To(self, aTo : time):
		self.___to = aTo

	def __init__(self):
		self.___from_62 : time = 0
		self.___to : time = 0

