#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import SwitchAndPosition
from typing import List, NewType

Duration = NewType("Duration", int)

class SwitchRelatedDelay(SwitchAndPosition.SwitchAndPosition):
	"""The position of a switch can influence the activation delay."""
	@property
	def Delay(self) -> Duration:
		return self.___delay
	
	@Delay.setter
	def Delay(self, aDelay : Duration):
		self.___delay = aDelay

	def __init__(self):
		self.___delay : Duration = 0
		"""The delay for activation to be considered when the switch is in the specified position."""

