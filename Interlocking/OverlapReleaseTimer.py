#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import anyAttribute
from RailML.Interlocking import tOverlapReleaseCondition
from typing import List, NewType

Duration = NewType("Duration", int)

class OverlapReleaseTimer(object):
	"""Details for timing the overlap release."""
	@property
	def TimerValue(self) -> Duration:
		return self.___timerValue
	@property
	def OverlapReleaseCondition(self) -> tOverlapReleaseCondition:
		return self.___overlapReleaseCondition
	@property
	def Rail3_anyAttribute(self) -> anyAttribute:
		return self.___rail3_anyAttribute

	@TimerValue.setter
	def TimerValue(self, aTimerValue : Duration):
		self.___timerValue = aTimerValue
	@OverlapReleaseCondition.setter
	def OverlapReleaseCondition(self, aOverlapReleaseCondition : tOverlapReleaseCondition):
		self.___overlapReleaseCondition = aOverlapReleaseCondition
	@Rail3_anyAttribute.setter
	def Rail3_anyAttribute(self, aRail3_anyAttribute : anyAttribute):
		self.___rail3_anyAttribute = aRail3_anyAttribute

	def __init__(self):
		self.___timerValue : Duration = 0
		"""The time period which has to be elapsed after the trigger condition and physical release of the overlap."""
		self.___overlapReleaseCondition : tOverlapReleaseCondition = tOverlapReleaseCondition.tOverlapReleaseCondition()
		# @AssociationType Interlocking.tOverlapReleaseCondition
		# @AssociationMultiplicity 0..1
		# """The condition to start the release timer."""
		self.___rail3_anyAttribute : anyAttribute = None	#TODO SOLVE THIS!
		"""# @AssociationKind Aggregation"""

