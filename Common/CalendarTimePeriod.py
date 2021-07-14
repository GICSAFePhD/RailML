#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common.TimePeriod import TimePeriod
import datetime	#ADDED TO FULFILL dateTime REQUIREMENT
from typing import List

class CalendarTimePeriod(TimePeriod):
	def setFrom_59(self, aFrom_59 : datetime):	#TODO DEFINES AS dateTime
		self.___from_59 = aFrom_59

	def getFrom_59(self) -> datetime:	#TODO DEFINES AS dateTime
		return self.___from_59

	def setTo(self, aTo : datetime):	#TODO DEFINES AS dateTime
		self.___to = aTo

	def getTo(self) -> datetime:	#TODO DEFINES AS dateTime
		return self.___to

	def __init__(self):
		self.___from_59 : datetime = None	#TODO DEFINES AS dateTime
		self.___to : datetime = None	#TODO DEFINES AS dateTime

