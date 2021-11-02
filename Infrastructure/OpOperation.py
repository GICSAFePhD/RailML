#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import tOpOperationalTypeExt, tOpTrafficTypeExt
from typing import List

class OpOperation(object):
	@property
	def OperationalType(self) -> tOpOperationalTypeExt:
		return self.___operationalType
	@property
	def TrafficType(self) -> tOpTrafficTypeExt:
		return self.___trafficType
	
	@OperationalType.setter
	def OperationalType(self, aOperationalType : tOpOperationalTypeExt):
		self.___operationalType = aOperationalType
	@TrafficType.setter
	def TrafficType(self, aTrafficType : tOpTrafficTypeExt):
		self.___trafficType = aTrafficType

	def __init__(self):
		self.___operationalType : tOpOperationalTypeExt = None
		# @AssociationType Infrastructure.tOpOperationalTypeExt
		# """operational characterization of the operational point"""
		self.___trafficType : tOpTrafficTypeExt = None
		# @AssociationType Infrastructure.tOpTrafficTypeExt
		# """definition of traffic type that is operating in this operational point"""