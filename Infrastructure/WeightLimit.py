#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Common import tWeightTons
from Common import tMeterloadTonsPerMeter
from Infrastructure import FunctionalInfrastructureEntity
from typing import List

class WeightLimit(FunctionalInfrastructureEntity):
	def setAxleLoad(self, aAxleLoad : tWeightTons):
		self.___axleLoad = aAxleLoad

	def getAxleLoad(self) -> tWeightTons:
		return self.___axleLoad

	def setMeterLoad(self, aMeterLoad : tMeterloadTonsPerMeter):
		self.___meterLoad = aMeterLoad

	def getMeterLoad(self) -> tMeterloadTonsPerMeter:
		return self.___meterLoad

	def __init__(self):
		self.___axleLoad : tWeightTons = None
		# @AssociationType Common.tWeightTons
		self.___meterLoad : tMeterloadTonsPerMeter = None
		# @AssociationType Common.tMeterloadTonsPerMeter

