#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import TimePeriod
import datetime	#ADDED TO FULFILL dateTime REQUIREMENT
from typing import List

class CalendarTimePeriod(TimePeriod.TimePeriod):
	@property
	def From_59(self) -> datetime:
		return self.___from_59
	@property
	def To(self) -> datetime:
		return self.___to
    
	@From_59.setter
	def From_59(self, aFrom_59 : datetime):
		self.___from_59 = aFrom_59
	@To.setter
	def To(self, aTo : datetime):
		self.___to = aTo

	def __init__(self):
		self.___from_59 : datetime = 0	#TODO DEFINES AS dateTime
		self.___to : datetime = 0	#TODO DEFINES AS dateTime

