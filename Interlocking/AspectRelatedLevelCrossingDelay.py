#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Interlocking import SignalAndAspect
from typing import List

class AspectRelatedLevelCrossingDelay(SignalAndAspect):
	"""The activation of the level crossing is delayed by a given duration if a signal shows a given aspect."""
	def setDelay(self, aDelay : duration):
		self.___delay = aDelay

	def getDelay(self) -> duration:
		return self.___delay

	def __init__(self):
		self.___delay : duration = None
		"""Delay between signal aspect detection and level crossing activation. This delay depends on the signalled speed of the approaching train hence on signal aspect."""

