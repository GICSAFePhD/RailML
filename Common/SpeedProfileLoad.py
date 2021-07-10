#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Common import tWeightTons
from Common import tMeterloadTonsPerMeter
from typing import List

class SpeedProfileLoad(object):
	def setMaxAxleLoad(self, aMaxAxleLoad : tWeightTons):
		self.___maxAxleLoad = aMaxAxleLoad

	def getMaxAxleLoad(self) -> tWeightTons:
		return self.___maxAxleLoad

	def setMaxMeterLoad(self, aMaxMeterLoad : tMeterloadTonsPerMeter):
		self.___maxMeterLoad = aMaxMeterLoad

	def getMaxMeterLoad(self) -> tMeterloadTonsPerMeter:
		return self.___maxMeterLoad

	def __init__(self):
		self.___maxAxleLoad : tWeightTons = None
		# @AssociationType Common.tWeightTons
		self.___maxMeterLoad : tMeterloadTonsPerMeter = None
		# @AssociationType Common.tMeterloadTonsPerMeter

