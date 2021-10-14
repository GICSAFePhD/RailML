#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import tOpOperationalTypeExt, tOpTrafficTypeExt
from typing import List

class OpOperation(object):
	@property
	def tOpOperationalTypeExt(self) -> tOpOperationalTypeExt:
		return self.___operationalType
	@property
	def tOpTrafficTypeExt(self) -> tOpTrafficTypeExt:
		return self.___trafficType
	
	@tOpOperationalTypeExt.setter
	def tOpOperationalTypeExt(self, atOpOperationalTypeExt : tOpOperationalTypeExt):
		self.___operationalType = atOpOperationalTypeExt
	@tOpTrafficTypeExt.setter
	def tOpTrafficTypeExt(self, atOpTrafficTypeExt : tOpTrafficTypeExt):
		self.___trafficType = atOpTrafficTypeExt

	def __init__(self):
		self.___operationalType : tOpOperationalTypeExt = tOpOperationalTypeExt.tOpOperationalTypeExt()
		# @AssociationType Infrastructure.tOpOperationalTypeExt
		# """operational characterization of the operational point"""
		self.___trafficType : tOpTrafficTypeExt = tOpTrafficTypeExt.tOpTrafficTypeExt()
		# @AssociationType Infrastructure.tOpTrafficTypeExt
		# """definition of traffic type that is operating in this operational point"""