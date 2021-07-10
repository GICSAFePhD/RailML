#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Interlocking import tOverlapReleaseCondition
from Common import anyAttribute
from typing import List

class OverlapReleaseTimer(object):
	"""Details for timing the overlap release."""
	def setTimerValue(self, aTimerValue : duration):
		self.___timerValue = aTimerValue

	def getTimerValue(self) -> duration:
		return self.___timerValue

	def setOverlapReleaseCondition(self, aOverlapReleaseCondition : tOverlapReleaseCondition):
		self.___overlapReleaseCondition = aOverlapReleaseCondition

	def getOverlapReleaseCondition(self) -> tOverlapReleaseCondition:
		return self.___overlapReleaseCondition

	def __init__(self):
		self.___timerValue : duration = None
		"""The time period which has to be elapsed after the trigger condition and physical release of the overlap."""
		self.___overlapReleaseCondition : tOverlapReleaseCondition = None
		# @AssociationType Interlocking.tOverlapReleaseCondition
		# @AssociationMultiplicity 0..1
		# """The condition to start the release timer."""
		self.___rail3_anyAttribute : anyAttribute = None
		"""# @AssociationKind Aggregation"""
