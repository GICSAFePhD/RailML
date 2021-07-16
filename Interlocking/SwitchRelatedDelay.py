#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking.SwitchAndPosition import SwitchAndPosition
from typing import List

class SwitchRelatedDelay(SwitchAndPosition):
	"""The position of a switch can influence the activation delay."""
	def setDelay(self, aDelay : int):	#TODO DEFINED AS duration
		self.___delay = aDelay

	def getDelay(self) -> int:	#TODO DEFINED AS durationc
		return self.___delay

	def __init__(self):
		self.___delay : int = None	#TODO DEFINED AS duration
		"""The delay for activation to be considered when the switch is in the specified position."""

