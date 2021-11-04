#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import TimePeriod
import time
from typing import List

class ClockTimePeriod(TimePeriod.TimePeriod):
	@property
	def From(self) -> time:
		return self.___from
	@property
	def To(self) -> time:
		return self.___to

	@From.setter
	def From(self, aFrom : time):
		self.___from = aFrom
	@To.setter
	def To(self, aTo : time):
		self.___to = aTo

	def __init__(self):
		self.___from : time = None
		self.___to : time = None

