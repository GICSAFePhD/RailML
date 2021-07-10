#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Common import tBitmaskWeek
from typing import List

class tElementBitmaskWeek(object):
	def setBitmask(self, aBitmask : tBitmaskWeek):
		self.___bitmask = aBitmask

	def getBitmask(self) -> tBitmaskWeek:
		return self.___bitmask

	def __init__(self):
		self.___bitmask : tBitmaskWeek = None
		# @AssociationType Common.tBitmaskWeek

