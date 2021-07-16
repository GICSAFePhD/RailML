#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking.EntityILref import EntityILref
from RailML.Interlocking.OverlapReleaseTimer import OverlapReleaseTimer
from RailML.Interlocking.EntityIL import EntityIL
from typing import List

class OverlapRelease(EntityIL):
	"""Overlap is set in lockstep with the route. The interlocking releases the overlap when it is safe to presume that an approaching train will not overrun a closed destination signal. When the train occupied the last section (or destination area), an overlap release timer starts running. The timer value is defined by operational rules and the approaching speed. Upon expiry, the interlocking releases the overlap. Overlap is released together with the route or after expiration of the release timer. Overlap is released after a defined time in a timer that starts from a timerTriggerPoint."""
	def setReleaseTriggerSection(self, aReleaseTriggerSection : EntityILref):
		self._releaseTriggerSection = aReleaseTriggerSection

	def getReleaseTriggerSection(self) -> EntityILref:
		return self._releaseTriggerSection

	def setOverlapReleaseTimer(self, *aOverlapReleaseTimer : OverlapReleaseTimer):
		self._overlapReleaseTimer = aOverlapReleaseTimer

	def getOverlapReleaseTimer(self) -> OverlapReleaseTimer:
		return self._overlapReleaseTimer

	def __init__(self):
		self._releaseTriggerSection : EntityILref = None
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 0..1
		# """The reference to the TVD section triggering the overlap release."""
		self._overlapReleaseTimer : OverlapReleaseTimer = None
		# @AssociationType Interlocking.OverlapReleaseTimer*
		# @AssociationMultiplicity 1..*
		# """Description of overlap release timer (duration, start condition)"""

