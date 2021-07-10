#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Interlocking import EntityILref
from Interlocking import EntityIL
from typing import List

class SignalDelayTime(EntityIL):
	"""Timer that maintains a signal at stop for a given duration after the level crossing was triggered."""
	def setDelay(self, aDelay : duration):
		self.___delay = aDelay

	def getDelay(self) -> duration:
		return self.___delay

	def setHasDelayedSignal(self, aHasDelayedSignal : EntityILref):
		self._hasDelayedSignal = aHasDelayedSignal

	def getHasDelayedSignal(self) -> EntityILref:
		return self._hasDelayedSignal

	def __init__(self):
		self.___delay : duration = None
		"""Time during which the signal remains closed. Starts counting when the level crossing is triggered."""
		self._hasDelayedSignal : EntityILref = None
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# """The reference to the signal."""

