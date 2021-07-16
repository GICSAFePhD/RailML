#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking.EntityILref import EntityILref
from RailML.Interlocking.EntityIL import EntityIL
from typing import List

class SignalDelayTime(EntityIL):
	"""Timer that maintains a signal at stop for a given duration after the level crossing was triggered."""
	def setDelay(self, aDelay : int):	#TODO DEFINED AS duration
		self.___delay = aDelay

	def getDelay(self) -> int:	#TODO DEFINED AS duration
		return self.___delay

	def setHasDelayedSignal(self, aHasDelayedSignal : EntityILref):
		self._hasDelayedSignal = aHasDelayedSignal

	def getHasDelayedSignal(self) -> EntityILref:
		return self._hasDelayedSignal

	def __init__(self):
		self.___delay : int = None	#TODO DEFINED AS duration
		"""Time during which the signal remains closed. Starts counting when the level crossing is triggered."""
		self._hasDelayedSignal : EntityILref = None
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# """The reference to the signal."""

