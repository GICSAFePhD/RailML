#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Common import tSpeedKmPerHour
from Common import tLengthM
from Common import tElementWithIDref
from typing import List

class LinePerformance(object):
	def setMaxSpeed(self, aMaxSpeed : tSpeedKmPerHour):
		self.___maxSpeed = aMaxSpeed

	def getMaxSpeed(self) -> tSpeedKmPerHour:
		return self.___maxSpeed

	def setMaxTrainLength(self, aMaxTrainLength : tLengthM):
		self.___maxTrainLength = aMaxTrainLength

	def getMaxTrainLength(self) -> tLengthM:
		return self.___maxTrainLength

	def setUsablePlatformLength(self, aUsablePlatformLength : tLengthM):
		self.___usablePlatformLength = aUsablePlatformLength

	def getUsablePlatformLength(self) -> tLengthM:
		return self.___usablePlatformLength

	def setAllowedLoadingGauge(self, *aAllowedLoadingGauge : tElementWithIDref*):
		self._allowedLoadingGauge = aAllowedLoadingGauge

	def getAllowedLoadingGauge(self) -> tElementWithIDref*:
		return self._allowedLoadingGauge

	def setAllowedWeight(self, *aAllowedWeight : tElementWithIDref*):
		self._allowedWeight = aAllowedWeight

	def getAllowedWeight(self) -> tElementWithIDref*:
		return self._allowedWeight

	def __init__(self):
		self.___maxSpeed : tSpeedKmPerHour = None
		# @AssociationType Common.tSpeedKmPerHour
		# """maximum line speed in km/h"""
		self.___maxTrainLength : tLengthM = None
		"""maximum allowed length for trains that run on this line"""
		self.___usablePlatformLength : tLengthM = None
		# @AssociationType Common.tLengthM
		# @AssociationType Common.tLengthM
		# """minimum platform length that is available in stations along that line"""
		self._allowedLoadingGauge : tElementWithIDref = None
		"""reference to a vehicle loading gauge that is allowed on this line"""
		self._allowedWeight : tElementWithIDref = None
		# @AssociationType Common.tElementWithIDref*
		# @AssociationMultiplicity 0..*
		# @AssociationType Common.tElementWithIDref*
		# @AssociationMultiplicity 0..*
		# """reference to a weight limit (axle load, metre load) that is allowed on that line"""

