#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Common import tBitmaskAny
from typing import List

class tElementBitmaskAny(object):
	def setBitmask(self, aBitmask : tBitmaskAny):
		self.___bitmask = aBitmask

	def getBitmask(self) -> tBitmaskAny:
		return self.___bitmask

	def __init__(self):
		self.___bitmask : tBitmaskAny = None
		# @AssociationType Common.tBitmaskAny

