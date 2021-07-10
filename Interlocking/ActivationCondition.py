#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Interlocking import tAndOr
from Interlocking import SwitchRelatedDelay
from Interlocking import AspectRelatedLevelCrossingDelay
from Interlocking import SignalDelayTime
from Interlocking import ApproachStartingDetector
from Interlocking import EntityIL
from typing import List

class ActivationCondition(EntityIL):
	"""The container to list all possible conditions for activating the level crossing."""
	def setAndOr(self, aAndOr : tAndOr):
		self.___andOr = aAndOr

	def getAndOr(self) -> tAndOr:
		return self.___andOr

	def setDelayBySwitchPosition(self, aDelayBySwitchPosition : SwitchRelatedDelay):
		self._delayBySwitchPosition = aDelayBySwitchPosition

	def getDelayBySwitchPosition(self) -> SwitchRelatedDelay:
		return self._delayBySwitchPosition

	def setAspectRelatedDelay(self, *aAspectRelatedDelay : AspectRelatedLevelCrossingDelay*):
		self._aspectRelatedDelay = aAspectRelatedDelay

	def getAspectRelatedDelay(self) -> AspectRelatedLevelCrossingDelay*:
		return self._aspectRelatedDelay

	def setSignalDelayTime(self, *aSignalDelayTime : SignalDelayTime*):
		self._signalDelayTime = aSignalDelayTime

	def getSignalDelayTime(self) -> SignalDelayTime*:
		return self._signalDelayTime

	def setActivatedBy(self, *aActivatedBy : ApproachStartingDetector*):
		self._activatedBy = aActivatedBy

	def getActivatedBy(self) -> ApproachStartingDetector*:
		return self._activatedBy

	def __init__(self):
		self.___andOr : tAndOr = None
		# @AssociationType Interlocking.tAndOr
		# """The logical combination of all activation conditions."""
		self._delayBySwitchPosition : SwitchRelatedDelay = None
		# @AssociationType Interlocking.SwitchRelatedDelay
		# @AssociationMultiplicity 0..1
		# """The activation can be delayed depending on the position of a switch."""
		self._aspectRelatedDelay : AspectRelatedLevelCrossingDelay = None
		# @AssociationType Interlocking.AspectRelatedLevelCrossingDelay*
		# @AssociationMultiplicity 0..*
		# """Activation of the level crossing may be delayed, depending on the aspect of the approach signal, thus, the activation delay timer depends on a) the signal and b) the signal aspect."""
		self._signalDelayTime : SignalDelayTime = None
		# @AssociationType Interlocking.SignalDelayTime*
		# @AssociationMultiplicity 0..*
		# """After activation of the level crossing the opening of a signal is delayed."""
		self._activatedBy : ApproachStartingDetector = None
		# @AssociationType Interlocking.ApproachStartingDetector*
		# @AssociationMultiplicity 1..*
		# """The activation of the level crossing is done by a train detection element."""

