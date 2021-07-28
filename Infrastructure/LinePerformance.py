#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tSpeedKmPerHour, tLengthM, tElementWithIDref
from typing import List

class LinePerformance(object):
	@property
	def MaxSpeed(self) -> tSpeedKmPerHour:
		return self.___maxSpeed
	@property
	def MaxTrainLength(self) -> tLengthM:
		return self.___maxTrainLength
	@property
	def UsablePlatformLength(self) -> tLengthM:
		return self.___usablePlatformLength
	@property
	def AllowedLoadingGauge(self) -> tElementWithIDref:
		return self.___allowedLoadingGauge
	@property
	def AllowedWeight(self) -> tElementWithIDref:
		return self.___allowedWeight

	@MaxSpeed.setter
	def MaxSpeed(self, aMaxSpeed : tSpeedKmPerHour):
		self.___maxSpeed = aMaxSpeed
	@MaxTrainLength.setter
	def MaxTrainLength(self, aMaxTrainLength : tLengthM):
		self.___maxTrainLength = aMaxTrainLength
	@UsablePlatformLength.setter
	def UsablePlatformLength(self, aUsablePlatformLength : tLengthM):
		self.___usablePlatformLength = aUsablePlatformLength
	@AllowedLoadingGauge.setter
	def AllowedLoadingGauge(self, aAllowedLoadingGauge : tElementWithIDref):
		self.___allowedLoadingGauge = aAllowedLoadingGauge
	@AllowedWeight.setter
	def AllowedWeight(self, aAllowedWeight : tElementWithIDref):
		self.___allowedWeight = aAllowedWeight

	def __init__(self):
		self.___maxSpeed : tSpeedKmPerHour = tSpeedKmPerHour.tSpeedKmPerHour()
		# @AssociationType Common.tSpeedKmPerHour
		# """maximum line speed in km/h"""
		self.___maxTrainLength : tLengthM = tLengthM.tLengthM()
		"""maximum allowed length for trains that run on this line"""
		self.___usablePlatformLength : tLengthM = tLengthM.tLengthM()
		# @AssociationType Common.tLengthM
		# @AssociationType Common.tLengthM
		# """minimum platform length that is available in stations along that line"""
		self.___allowedLoadingGauge : tElementWithIDref = tElementWithIDref.tElementWithIDref()
		"""reference to a vehicle loading gauge that is allowed on this line"""
		self.___allowedWeight : tElementWithIDref = tElementWithIDref.tElementWithIDref()
		# @AssociationType Common.tElementWithIDref*
		# @AssociationMultiplicity 0..*
		# @AssociationType Common.tElementWithIDref*
		# @AssociationMultiplicity 0..*
		# """reference to a weight limit (axle load, metre load) that is allowed on that line"""

