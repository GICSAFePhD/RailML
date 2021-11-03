#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import EntityILref, EntityIL
from typing import List, NewType

Duration = NewType("Duration", int)

class ApproachStartingDetector(EntityIL.EntityIL):
	"""Train detection device, commonly an axle counter, track section, track joint or treadle that activates a level crossing. Also known as Approach Starting. This is the detection point that is the most remote from the level crossing. The approach monitoring zone is situated in between the approach starting detector(s) and the level crossing, i.e. every detector in this zone activates the level crossing. Use the any wildcard to provide a textual description of the approach starting detector is needed."""
	@property
	def Delay(self) -> Duration:
		return self.___delay
	@property
	def RefersTo(self) -> EntityILref:
		return self.___refersTo

	@Delay.setter
	def Delay(self, aDelay : Duration):
		self.___delay = aDelay
	@RefersTo.setter
	def RefersTo(self, aRefersTo : EntityILref):
		self.___refersTo = aRefersTo

	def __init__(self):
		super().__init__()
		self.___delay : Duration = None
		"""The level crossing is activated only after a given delay. This delay doesn't depend on any aspect. If there's a delay that depends on signalled speed, please use the aspectRelatedLevelCrossingDelay.
		The timer starts running when the first train axle triggers the train detector."""
		self.___refersTo : EntityILref = None
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# """The reference to the train detection element in infrastructure."""