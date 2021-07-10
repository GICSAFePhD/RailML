#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Common import tBrakeTypeExt
from Common import tAirBrakeApplicationDirection
from Common import tBrakePercentage
from typing import List

class SpeedProfileBraking(object):
	def setBrakeType(self, aBrakeType : tBrakeTypeExt):
		self.___brakeType = aBrakeType

	def getBrakeType(self) -> tBrakeTypeExt:
		return self.___brakeType

	def setAirBrakeApplicationPosition(self, aAirBrakeApplicationPosition : tAirBrakeApplicationDirection):
		self.___airBrakeApplicationPosition = aAirBrakeApplicationPosition

	def getAirBrakeApplicationPosition(self) -> tAirBrakeApplicationDirection:
		return self.___airBrakeApplicationPosition

	def setMinBrakePercentage(self, aMinBrakePercentage : tBrakePercentage):
		self.___minBrakePercentage = aMinBrakePercentage

	def getMinBrakePercentage(self) -> tBrakePercentage:
		return self.___minBrakePercentage

	def __init__(self):
		self.___brakeType : tBrakeTypeExt = None
		# @AssociationType Common.tBrakeTypeExt
		# """vacuum or compressed air brake, hand brake, parking brake, cable brake"""
		self.___airBrakeApplicationPosition : tAirBrakeApplicationDirection = None
		# @AssociationType Common.tAirBrakeApplicationDirection
		# """base brake switch: one of G, P or R"""
		self.___minBrakePercentage : tBrakePercentage = None
		# @AssociationType Common.tBrakePercentage
		# """minimum brake percentage of the train"""

