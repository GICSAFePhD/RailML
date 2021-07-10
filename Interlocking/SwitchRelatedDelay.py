#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Interlocking import SwitchAndPosition
from typing import List

class SwitchRelatedDelay(SwitchAndPosition):
	"""The position of a switch can influence the activation delay."""
	def setDelay(self, aDelay : duration):
		self.___delay = aDelay

	def getDelay(self) -> duration:
		return self.___delay

	def __init__(self):
		self.___delay : duration = None
		"""The delay for activation to be considered when the switch is in the specified position."""

