#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import tAndOr, SwitchRelatedDelay, AspectRelatedLevelCrossingDelay, SignalDelayTime, ApproachStartingDetector, EntityIL
from typing import List

class ActivationCondition(EntityIL.EntityIL):
	"""The container to list all possible conditions for activating the level crossing."""
	@property
	def AndOr(self) -> tAndOr:
		return self.___andOr
	@property
	def DelayBySwitchPosition(self) -> SwitchRelatedDelay:
		return self.___delayBySwitchPosition
	@property
	def AspectRelatedDelay(self) -> AspectRelatedLevelCrossingDelay:
		return self.___aspectRelatedDelay
	@property
	def SignalDelayTime(self) -> SignalDelayTime:
		return self.___signalDelayTime
	@property
	def ActivatedBy(self) -> ApproachStartingDetector:
		return self.___activatedBy

	@AndOr.setter
	def AndOr(self, aAndOr : tAndOr):
		self.___andOr = aAndOr
	@DelayBySwitchPosition.setter
	def DelayBySwitchPosition(self, aDelayBySwitchPosition : SwitchRelatedDelay):
		self.___delayBySwitchPosition = aDelayBySwitchPosition
	@AspectRelatedDelay.setter
	def AspectRelatedDelay(self, *aAspectRelatedDelay : AspectRelatedLevelCrossingDelay):
		self.___aspectRelatedDelay = aAspectRelatedDelay
	@SignalDelayTime.setter
	def SignalDelayTime(self, *aSignalDelayTime : SignalDelayTime):
		self.___signalDelayTime = aSignalDelayTime
	@ActivatedBy.setter
	def ActivatedBy(self, *aActivatedBy : ApproachStartingDetector):
		self.___activatedBy = aActivatedBy

	def __init__(self):
		super().__init__()
		self.___andOr : tAndOr = tAndOr.tAndOr()
		# @AssociationType Interlocking.tAndOr
		# """The logical combination of all activation conditions."""
		self.___delayBySwitchPosition : SwitchRelatedDelay = SwitchRelatedDelay.SwitchRelatedDelay()
		# @AssociationType Interlocking.SwitchRelatedDelay
		# @AssociationMultiplicity 0..1
		# """The activation can be delayed depending on the position of a switch."""
		self.___aspectRelatedDelay : AspectRelatedLevelCrossingDelay = AspectRelatedLevelCrossingDelay.AspectRelatedLevelCrossingDelay()
		# @AssociationType Interlocking.AspectRelatedLevelCrossingDelay*
		# @AssociationMultiplicity 0..*
		# """Activation of the level crossing may be delayed, depending on the aspect of the approach signal, thus, the activation delay timer depends on a) the signal and b) the signal aspect."""
		self.___signalDelayTime : SignalDelayTime = SignalDelayTime.SignalDelayTime()
		# @AssociationType Interlocking.SignalDelayTime*
		# @AssociationMultiplicity 0..*
		# """After activation of the level crossing the opening of a signal is delayed."""
		self.___activatedBy : ApproachStartingDetector = ApproachStartingDetector.ApproachStartingDetector()
		# @AssociationType Interlocking.ApproachStartingDetector*
		# @AssociationMultiplicity 1..*
		# """The activation of the level crossing is done by a train detection element."""