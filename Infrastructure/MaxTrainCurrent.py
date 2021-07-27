#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tCurrentAmpere
from RailML.Infrastructure import tOperationalTrainType
from typing import List

class MaxTrainCurrent(object):
	@property
	def MaxCurrent(self) -> tCurrentAmpere:
		return self.___maxCurrent
	@property
	def TrainType(self) -> tOperationalTrainType:
		return self.___trainType
	@property
	def OperationType(self) -> int:
		return self.___operationType
	@property
	def ValidFor(self) -> int:
		return self.___validFor

	@MaxCurrent.setter
	def MaxCurrent(self, aMaxCurrent : tCurrentAmpere):
		self.___maxCurrent = aMaxCurrent
	@TrainType.setter
	def TrainType(self, aTrainType : tOperationalTrainType):
		self.___trainType = aTrainType
	@OperationType.setter
	def OperationType(self, aOperationType : int):
		self.___operationType = aOperationType
	@ValidFor.setter
	def ValidFor(self, aValidFor : int):
		self.___validFor = aValidFor

	def __init__(self):
		self.___maxCurrent : tCurrentAmpere = tCurrentAmpere.tCurrentAmpere()
		# @AssociationType Common.tCurrentAmpere
		# """maximum allowed current in Ampere"""
		self.___trainType : tOperationalTrainType = tOperationalTrainType.tOperationalTrainType()
		# @AssociationType Infrastructure.tOperationalTrainType
		# """train category for which the maximum train current constraint is valid"""
		self.___operationType : int = 0
		"""type of operation for maximum train current: standstill or driving"""
		self.___validFor : int = 0
		"""application of maximum train current: train or pantograph"""

