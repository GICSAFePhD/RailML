#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tLengthM, tSpeedKmPerHour
from typing import List

class PantographSpacing(object):
	@property
	def NumberPantographsRaised(self) -> int:
		return self.___numberPantographsRaised
	@property
	def SpacingPantographsRaised(self) -> tLengthM:
		return self.___spacingPantographsRaised
	@property
	def Speed4PantographSpacing(self) -> tSpeedKmPerHour:
		return self.___speed4PantographSpacing

	@NumberPantographsRaised.setter
	def GradieNumberPantographsRaisedntCurve(self, aNumberPantographsRaised : int):
		self.___numberPantographsRaised = aNumberPantographsRaised
	@SpacingPantographsRaised.setter
	def SpacingPantographsRaised(self, aSpacingPantographsRaised : tLengthM):
		self.___spacingPantographsRaised = aSpacingPantographsRaised
	@Speed4PantographSpacing.setter
	def Speed4PantographSpacing(self, aSpeed4PantographSpacing : tSpeedKmPerHour):
		self.___speed4PantographSpacing = aSpeed4PantographSpacing

	def __init__(self):
		self.___numberPantographsRaised : int = 0
		"""number of pantographs raised simultaneously on moving train"""
		self.___spacingPantographsRaised : tLengthM = tLengthM.tLengthM()
		# @AssociationType Common.tLengthM
		# """minimum spacing between raised pantographs of a train, in [m]"""
		self.___speed4PantographSpacing : tSpeedKmPerHour = tSpeedKmPerHour.tSpeedKmPerHour()
		# @AssociationType Common.tSpeedKmPerHour
		# """related maximum speed for the given pantograph spacing limit, in [km/h]"""

