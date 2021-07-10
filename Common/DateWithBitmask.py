#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Common import tBitmaskAny
from typing import List

class DateWithBitmask(object):
	def setDate(self, aDate : date):
		self.___date = aDate

	def getDate(self) -> date:
		return self.___date

	def setBitmask(self, aBitmask : tBitmaskAny):
		self.___bitmask = aBitmask

	def getBitmask(self) -> tBitmaskAny:
		return self.___bitmask

	def __init__(self):
		self.___date : date = None
		self.___bitmask : tBitmaskAny = None
		# @AssociationType Common.tBitmaskAny

