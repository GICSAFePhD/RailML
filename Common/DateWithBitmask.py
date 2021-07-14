#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common.tBitmaskAny import tBitmaskAny
import datetime
from typing import List

class DateWithBitmask(object):
	def setDate(self, aDate : datetime):	#TODO DEFINED AS date
		self.___date = aDate

	def getDate(self) -> datetime:	#TODO DEFINED AS date
		return self.___date

	def setBitmask(self, aBitmask : tBitmaskAny):
		self.___bitmask = aBitmask

	def getBitmask(self) -> tBitmaskAny:
		return self.___bitmask

	def __init__(self):
		self.___date : datetime = None	#TODO DEFINED AS date
		self.___bitmask : tBitmaskAny = None
		# @AssociationType Common.tBitmaskAny

