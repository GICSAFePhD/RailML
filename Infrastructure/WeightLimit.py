#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tWeightTons, tMeterloadTonsPerMeter
from RailML.Infrastructure import FunctionalInfrastructureEntity
from typing import List

class WeightLimit(FunctionalInfrastructureEntity.FunctionalInfrastructureEntity):
	@property
	def AxleLoad(self) -> tWeightTons:
		return self.___axleLoad
	@property
	def MeterLoad(self) -> tMeterloadTonsPerMeter:
		return self.___meterLoad
	
	@AxleLoad.setter
	def AxleLoad(self, aAxleLoad : tWeightTons):
		self.___axleLoad = aAxleLoad
	@MeterLoad.setter
	def MeterLoad(self, aMeterLoad : tMeterloadTonsPerMeter):
		self.___meterLoad = aMeterLoad

	def __init__(self):
		self.___axleLoad : tWeightTons = None
		# @AssociationType Common.tWeightTons
		self.___meterLoad : tMeterloadTonsPerMeter = None
		# @AssociationType Common.tMeterloadTonsPerMeter

