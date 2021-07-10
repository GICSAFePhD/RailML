#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Common import TimePeriod
from typing import List

class CalendarTimePeriod(TimePeriod):
	def setFrom_59(self, aFrom_59 : dateTime):
		self.___from_59 = aFrom_59

	def getFrom_59(self) -> dateTime:
		return self.___from_59

	def setTo(self, aTo : dateTime):
		self.___to = aTo

	def getTo(self) -> dateTime:
		return self.___to

	def __init__(self):
		self.___from_59 : dateTime = None
		self.___to : dateTime = None

