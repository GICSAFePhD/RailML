#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common.tCurrentAmpere import tCurrentAmpere
from RailML.Infrastructure.tOperationalTrainType import tOperationalTrainType
from typing import List

class MaxTrainCurrent(object):
	def setMaxCurrent(self, aMaxCurrent : tCurrentAmpere):
		self.___maxCurrent = aMaxCurrent

	def getMaxCurrent(self) -> tCurrentAmpere:
		return self.___maxCurrent

	def setTrainType(self, aTrainType : tOperationalTrainType):
		self.___trainType = aTrainType

	def getTrainType(self) -> tOperationalTrainType:
		return self.___trainType

	def setOperationType(self, aOperationType : int):
		self.___operationType = aOperationType

	def getOperationType(self) -> int:
		return self.___operationType

	def setValidFor(self, aValidFor : int):
		self.___validFor = aValidFor

	def getValidFor(self) -> int:
		return self.___validFor

	def __init__(self):
		self.___maxCurrent : tCurrentAmpere = None
		# @AssociationType Common.tCurrentAmpere
		# """maximum allowed current in Ampere"""
		self.___trainType : tOperationalTrainType = None
		# @AssociationType Infrastructure.tOperationalTrainType
		# """train category for which the maximum train current constraint is valid"""
		self.___operationType : int = None
		"""type of operation for maximum train current: standstill or driving"""
		self.___validFor : int = None
		"""application of maximum train current: train or pantograph"""

