#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import EntityILref, OverlapReleaseTimer, EntityIL
from typing import List

class OverlapRelease(EntityIL.EntityIL):
	"""Overlap is set in lockstep with the route. The interlocking releases the overlap when it is safe to presume that an approaching train will not overrun a closed destination signal. When the train occupied the last section (or destination area), an overlap release timer starts running. The timer value is defined by operational rules and the approaching speed. Upon expiry, the interlocking releases the overlap. Overlap is released together with the route or after expiration of the release timer. Overlap is released after a defined time in a timer that starts from a timerTriggerPoint."""
	@property
	def ReleaseTriggerSection(self) -> EntityILref:
		return self.___releaseTriggerSection
	@property
	def OverlapReleaseTimer(self) -> OverlapReleaseTimer:
		return self.___overlapReleaseTimer

	@ReleaseTriggerSection.setter
	def ReleaseTriggerSection(self, aReleaseTriggerSection : EntityILref):
		self.___releaseTriggerSection = aReleaseTriggerSection
	@OverlapReleaseTimer.setter
	def OverlapReleaseTimer(self, *aOverlapReleaseTimer : OverlapReleaseTimer):
		self.___overlapReleaseTimer = aOverlapReleaseTimer

	def __init__(self):
		self.___releaseTriggerSection : EntityILref = EntityILref.EntityILref()
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 0..1
		# """The reference to the TVD section triggering the overlap release."""
		self.___overlapReleaseTimer : OverlapReleaseTimer = OverlapReleaseTimer.OverlapReleaseTimer()
		# @AssociationType Interlocking.OverlapReleaseTimer*
		# @AssociationMultiplicity 1..*
		# """Description of overlap release timer (duration, start condition)"""

