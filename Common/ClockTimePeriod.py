#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Common import TimePeriod
from typing import List

class ClockTimePeriod(TimePeriod):
	def setFrom_62(self, aFrom_62 : time):
		self.___from_62 = aFrom_62

	def getFrom_62(self) -> time:
		return self.___from_62

	def setTo(self, aTo : time):
		self.___to = aTo

	def getTo(self) -> time:
		return self.___to

	def __init__(self):
		self.___from_62 : time = None
		self.___to : time = None

