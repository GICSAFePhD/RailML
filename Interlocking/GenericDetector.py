#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking.EntityILref import EntityILref
from RailML.Interlocking.LogicalDevice import LogicalDevice
from typing import List

class GenericDetector(LogicalDevice):
	"""Detectors are devices detecting the exceeding of a particular characteristic and providing an output to the interlocking. Depending on the function it may influence the route signalling."""
	def setAffectsRouteSignalling(self, aAffectsRouteSignalling : int):	#TODO DEFINED AS LONG
		self.___affectsRouteSignalling = aAffectsRouteSignalling

	def getAffectsRouteSignalling(self) -> int:	#TODO DEFINED AS LONG
		return self.___affectsRouteSignalling

	def setAllowsSingleOverride(self, aAllowsSingleOverride : int):	#TODO DEFINED AS LONG
		self.___allowsSingleOverride = aAllowsSingleOverride

	def getAllowsSingleOverride(self) -> int:	#TODO DEFINED AS LONG
		return self.___allowsSingleOverride

	def setAllowsPermanentOverride(self, aAllowsPermanentOverride : int):	#TODO DEFINED AS LONG
		self.___allowsPermanentOverride = aAllowsPermanentOverride

	def getAllowsPermanentOverride(self) -> int:	#TODO DEFINED AS LONG
		return self.___allowsPermanentOverride

	def setHasTriggeredSelfTest(self, aHasTriggeredSelfTest : int):	#TODO DEFINED AS LONG
		self.___hasTriggeredSelfTest = aHasTriggeredSelfTest

	def getHasTriggeredSelfTest(self) -> int:	#TODO DEFINED AS LONG
		return self.___hasTriggeredSelfTest

	def setSelfTestToleranceTime(self, aSelfTestToleranceTime : int):	#TODO DEFINED AS duration
		self.___selfTestToleranceTime = aSelfTestToleranceTime

	def getSelfTestToleranceTime(self) -> int:	#TODO DEFINED AS duration
		return self.___selfTestToleranceTime

	def setSelfTestInterval(self, aSelfTestInterval : int):	#TODO DEFINED AS duration
		self.___selfTestInterval = aSelfTestInterval

	def getSelfTestInterval(self) -> int:	#TODO DEFINED AS duration
		return self.___selfTestInterval

	def setDetectorType(self, aDetectorType : EntityILref):
		self._detectorType = aDetectorType

	def getDetectorType(self) -> EntityILref:
		return self._detectorType

	def __init__(self):
		self.___affectsRouteSignalling : int = None	#TODO DEFINED AS LONG
		"""indication whether the signalling of a related route is affected by the detector status"""
		self.___allowsSingleOverride : int = None	#TODO DEFINED AS LONG
		"""The detector output may be overridden once by special command."""
		self.___allowsPermanentOverride : int = None	#TODO DEFINED AS LONG
		"""The detector output may be permanently overridden by special command."""
		self.___hasTriggeredSelfTest : int = None	#TODO DEFINED AS LONG
		"""The detector may have a self-test which is to be triggered from the interlocking."""
		self.___selfTestToleranceTime : int = None	#TODO DEFINED AS duration
		"""The time period for which the detector output shall be tolerated due to running self-test."""
		self.___selfTestInterval : int = None	#TODO DEFINED AS duration
		"""The interval at which the self-test is running, i.e. automatically initiated or triggered from interlocking."""
		self._detectorType : EntityILref = None
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# """The reference to the particular detector type."""

