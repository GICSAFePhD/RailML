#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Infrastructure import tOpOperationalTypeExt
from Infrastructure import tOpTrafficTypeExt
from typing import List

class OpOperation(object):
	def setOperationalType(self, aOperationalType : tOpOperationalTypeExt):
		self.___operationalType = aOperationalType

	def getOperationalType(self) -> tOpOperationalTypeExt:
		return self.___operationalType

	def setTrafficType(self, aTrafficType : tOpTrafficTypeExt):
		self.___trafficType = aTrafficType

	def getTrafficType(self) -> tOpTrafficTypeExt:
		return self.___trafficType

	def __init__(self):
		self.___operationalType : tOpOperationalTypeExt = None
		# @AssociationType Infrastructure.tOpOperationalTypeExt
		# """operational characterization of the operational point"""
		self.___trafficType : tOpTrafficTypeExt = None
		# @AssociationType Infrastructure.tOpTrafficTypeExt
		# """definition of traffic type that is operating in this operational point"""

