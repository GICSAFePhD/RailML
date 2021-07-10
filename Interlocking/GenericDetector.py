#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Interlocking import EntityILref
from Interlocking import LogicalDevice
from typing import List

class GenericDetector(LogicalDevice):
	"""Detectors are devices detecting the exceeding of a particular characteristic and providing an output to the interlocking. Depending on the function it may influence the route signalling."""
	def setAffectsRouteSignalling(self, aAffectsRouteSignalling : long):
		self.___affectsRouteSignalling = aAffectsRouteSignalling

	def getAffectsRouteSignalling(self) -> long:
		return self.___affectsRouteSignalling

	def setAllowsSingleOverride(self, aAllowsSingleOverride : long):
		self.___allowsSingleOverride = aAllowsSingleOverride

	def getAllowsSingleOverride(self) -> long:
		return self.___allowsSingleOverride

	def setAllowsPermanentOverride(self, aAllowsPermanentOverride : long):
		self.___allowsPermanentOverride = aAllowsPermanentOverride

	def getAllowsPermanentOverride(self) -> long:
		return self.___allowsPermanentOverride

	def setHasTriggeredSelfTest(self, aHasTriggeredSelfTest : long):
		self.___hasTriggeredSelfTest = aHasTriggeredSelfTest

	def getHasTriggeredSelfTest(self) -> long:
		return self.___hasTriggeredSelfTest

	def setSelfTestToleranceTime(self, aSelfTestToleranceTime : duration):
		self.___selfTestToleranceTime = aSelfTestToleranceTime

	def getSelfTestToleranceTime(self) -> duration:
		return self.___selfTestToleranceTime

	def setSelfTestInterval(self, aSelfTestInterval : duration):
		self.___selfTestInterval = aSelfTestInterval

	def getSelfTestInterval(self) -> duration:
		return self.___selfTestInterval

	def setDetectorType(self, aDetectorType : EntityILref):
		self._detectorType = aDetectorType

	def getDetectorType(self) -> EntityILref:
		return self._detectorType

	def __init__(self):
		self.___affectsRouteSignalling : long = None
		"""indication whether the signalling of a related route is affected by the detector status"""
		self.___allowsSingleOverride : long = None
		"""The detector output may be overridden once by special command."""
		self.___allowsPermanentOverride : long = None
		"""The detector output may be permanently overridden by special command."""
		self.___hasTriggeredSelfTest : long = None
		"""The detector may have a self-test which is to be triggered from the interlocking."""
		self.___selfTestToleranceTime : duration = None
		"""The time period for which the detector output shall be tolerated due to running self-test."""
		self.___selfTestInterval : duration = None
		"""The interval at which the self-test is running, i.e. automatically initiated or triggered from interlocking."""
		self._detectorType : EntityILref = None
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# """The reference to the particular detector type."""

