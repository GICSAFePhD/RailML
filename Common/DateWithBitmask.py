#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tBitmaskAny
import datetime
from typing import List

class DateWithBitmask(object):
	@property
	def Date(self) -> datetime:
		return self.___date
	@property
	def Bitmask(self) -> tBitmaskAny:
		return self.___bitmask

	@Date.setter
	def Date(self, aDate : datetime):
		self.___date = aDate
	@Bitmask.setter
	def Bitmask(self, aBitmask : tBitmaskAny):
		self.___bitmask = aBitmask

	def __init__(self):
		self.___date : datetime = 0	#TODO DEFINED AS date
		self.___bitmask : tBitmaskAny = tBitmaskAny.tBitmaskAny()
		# @AssociationType Common.tBitmaskAny

