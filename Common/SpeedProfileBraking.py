#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tBrakeTypeExt, tAirBrakeApplicationDirection, tBrakePercentage
from typing import List

class SpeedProfileBraking(object):
	@property
	def tBrakeTypeExt(self) -> tBrakeTypeExt:
		return self.___brakeType
	@property
	def tAirBrakeApplicationDirection(self) -> tAirBrakeApplicationDirection:
		return self.___airBrakeApplicationPosition
	@property
	def tBrakePercentage(self) -> tBrakePercentage:
		return self.___minBrakePercentage

	@tBrakeTypeExt.setter
	def tBrakeTypeExt(self, atBrakeTypeExt : tBrakeTypeExt):
		self.___brakeType = atBrakeTypeExt
	@tAirBrakeApplicationDirection.setter
	def tAirBrakeApplicationDirection(self, atAirBrakeApplicationDirection : tAirBrakeApplicationDirection):
		self.___airBrakeApplicationPosition = atAirBrakeApplicationDirection
	@tBrakePercentage.setter
	def tBrakePercentage(self, atBrakePercentage : tBrakePercentage):
		self.___minBrakePercentage = atBrakePercentage

	def __init__(self):
		self.___brakeType : tBrakeTypeExt = tBrakeTypeExt.tBrakeTypeExt()
		# @AssociationType Common.tBrakeTypeExt
		# """vacuum or compressed air brake, hand brake, parking brake, cable brake"""
		self.___airBrakeApplicationPosition : tAirBrakeApplicationDirection = tAirBrakeApplicationDirection.tAirBrakeApplicationDirection()
		# @AssociationType Common.tAirBrakeApplicationDirection
		# """base brake switch: one of G, P or R"""
		self.___minBrakePercentage : tBrakePercentage = tBrakePercentage.tBrakePercentage()
		# @AssociationType Common.tBrakePercentage
		# """minimum brake percentage of the train"""

