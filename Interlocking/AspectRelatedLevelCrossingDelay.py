#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import SignalAndAspect
from typing import List, NewType
Duration = NewType("Duration", int)

class AspectRelatedLevelCrossingDelay(SignalAndAspect.SignalAndAspect):
	"""The activation of the level crossing is delayed by a given duration if a signal shows a given aspect."""
	@property
	def Delay(self) -> Duration:
		return self.___delay
	
	@Delay.setter
	def Delay(self, aDelay : Duration):
		self.___delay = aDelay

	def __init__(self):
		self.___delay : Duration = 0
		"""Delay between signal aspect detection and level crossing activation. This delay depends on the signalled speed of the approaching train hence on signal aspect."""

