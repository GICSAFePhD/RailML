#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import EntityILref, EntityIL
from typing import List, NewType

Duration = NewType("Duration", int)

class SignalDelayTime(EntityIL.EntityIL):
	"""Timer that maintains a signal at stop for a given duration after the level crossing was triggered."""
	@property
	def Delay(self) -> Duration:
		return self.___delay
	@property
	def HasDelayedSignal(self) -> EntityILref:
		return self.___hasDelayedSignal

	@Delay.setter
	def Delay(self, aDelay : Duration):
		self.___delay = aDelay
	@HasDelayedSignal.setter
	def HasDelayedSignal(self, aHasDelayedSignal : EntityILref):
		self.___hasDelayedSignal = aHasDelayedSignal

	def __init__(self):
		self.___delay : Duration = 0
		"""Time during which the signal remains closed. Starts counting when the level crossing is triggered."""
		self.___hasDelayedSignal : EntityILref = EntityILref.EntityILref()
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# """The reference to the signal."""

