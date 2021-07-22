#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tWeightTons, tMeterloadTonsPerMeter
from typing import List

class SpeedProfileLoad(object):
	@property
	def tWeightTons(self) -> tWeightTons:
		return self.___maxAxleLoad
	@property
	def tMeterloadTonsPerMeter(self) -> tMeterloadTonsPerMeter:
		return self.___maxMeterLoad

	@tWeightTons.setter
	def tWeightTons(self, atWeightTons : tWeightTons):
		self.___maxAxleLoad = atWeightTons
	@tMeterloadTonsPerMeter.setter
	def tMeterloadTonsPerMeter(self, atMeterloadTonsPerMeter : tMeterloadTonsPerMeter):
		self.___maxMeterLoad = tMeterloadTonsPerMeter

	def __init__(self):
		self.___maxAxleLoad : tWeightTons = tWeightTons.tWeightTons()
		# @AssociationType Common.tWeightTons
		self.___maxMeterLoad : tMeterloadTonsPerMeter = tMeterloadTonsPerMeter.tMeterloadTonsPerMeter()
		# @AssociationType Common.tMeterloadTonsPerMeter

