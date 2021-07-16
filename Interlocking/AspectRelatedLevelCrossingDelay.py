#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking.SignalAndAspect import SignalAndAspect
from typing import List

class AspectRelatedLevelCrossingDelay(SignalAndAspect):
	"""The activation of the level crossing is delayed by a given duration if a signal shows a given aspect."""
	def setDelay(self, aDelay : int):	#TODO DEFINED AS duration
		self.___delay = aDelay

	def getDelay(self) -> int:	#TODO DEFINED AS duration
		return self.___delay

	def __init__(self):
		self.___delay : int = None	#TODO DEFINED AS duration
		"""Delay between signal aspect detection and level crossing activation. This delay depends on the signalled speed of the approaching train hence on signal aspect."""

