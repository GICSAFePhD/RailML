#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import EntityILref, LogicalDevice
from typing import List, NewType
Long = NewType("Long", int)
Duration = NewType("Duration", int)

class GenericDetector(LogicalDevice.LogicalDevice):
	"""Detectors are devices detecting the exceeding of a particular characteristic and providing an output to the interlocking. Depending on the function it may influence the route signalling."""
	@property
	def AffectsRouteSignalling(self) -> Long:
		return self.___affectsRouteSignalling
	@property
	def AllowsSingleOverride(self) -> Long:
		return self.___allowsSingleOverride
	@property
	def AllowsPermanentOverride(self) -> Long:
		return self.___allowsPermanentOverride
	@property
	def HasTriggeredSelfTest(self) -> Long:
		return self.___hasTriggeredSelfTest
	@property
	def SelfTestToleranceTime(self) -> Duration:
		return self.___selfTestToleranceTime
	@property
	def SelfTestInterval(self) -> Duration:
		return self.___selfTestInterval
	@property
	def DetectorType(self) -> EntityILref:
		return self.___detectorType

	@AffectsRouteSignalling.setter
	def AffectsRouteSignalling(self, aAffectsRouteSignalling : Long):
		self.___affectsRouteSignalling = aAffectsRouteSignalling
	@AllowsSingleOverride.setter
	def AllowsSingleOverride(self, aAllowsSingleOverride : Long):
		self.___allowsSingleOverride = aAllowsSingleOverride
	@AllowsPermanentOverride.setter
	def AllowsPermanentOverride(self, aAllowsPermanentOverride : Long):
		self.___allowsPermanentOverride = aAllowsPermanentOverride
	@HasTriggeredSelfTest.setter
	def HasTriggeredSelfTest(self, aHasTriggeredSelfTest : Long):
		self.___hasTriggeredSelfTest = aHasTriggeredSelfTest
	@SelfTestToleranceTime.setter
	def SelfTestToleranceTime(self, aSelfTestToleranceTime : Duration):
		self.___selfTestToleranceTime = aSelfTestToleranceTime
	@SelfTestInterval.setter
	def SelfTestInterval(self, aSelfTestInterval : Duration):
		self.___selfTestInterval = aSelfTestInterval
	@DetectorType.setter
	def DetectorType(self, aDetectorType : EntityILref):
		self.___detectorType = aDetectorType

	def __init__(self):
		self.___affectsRouteSignalling : Long = 0
		"""indication whether the signalling of a related route is affected by the detector status"""
		self.___allowsSingleOverride : Long = 0
		"""The detector output may be overridden once by special command."""
		self.___allowsPermanentOverride : Long = 0
		"""The detector output may be permanently overridden by special command."""
		self.___hasTriggeredSelfTest : Long = 0
		"""The detector may have a self-test which is to be triggered from the interlocking."""
		self.___selfTestToleranceTime : Duration = 0
		"""The time period for which the detector output shall be tolerated due to running self-test."""
		self.___selfTestInterval : Duration = 0
		"""The interval at which the self-test is running, i.e. automatically initiated or triggered from interlocking."""
		self.___detectorType : EntityILref = EntityILref.EntityILref()
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# """The reference to the particular detector type."""

