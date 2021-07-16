#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking.EntityILref import EntityILref
from RailML.Interlocking.EntityIL import EntityIL
from typing import List

class ApproachStartingDetector(EntityIL):
	"""Train detection device, commonly an axle counter, track section, track joint or treadle that activates a level crossing. Also known as Approach Starting. This is the detection point that is the most remote from the level crossing. The approach monitoring zone is situated in between the approach starting detector(s) and the level crossing, i.e. every detector in this zone activates the level crossing. Use the any wildcard to provide a textual description of the approach starting detector is needed."""
	def setDelay(self, aDelay : int):	#TODO DEFINED AS duration
		self.___delay = aDelay

	def getDelay(self) -> int:	#TODO DEFINED AS duration
		return self.___delay

	def setRefersTo(self, aRefersTo : EntityILref):
		self._refersTo = aRefersTo

	def getRefersTo(self) -> EntityILref:
		return self._refersTo

	def __init__(self):
		self.___delay : int = None	#TODO DEFINED AS duration
		"""The level crossing is activated only after a given delay. This delay doesn't depend on any aspect. If there's a delay that depends on signalled speed, please use the aspectRelatedLevelCrossingDelay.
		The timer starts running when the first train axle triggers the train detector."""
		self._refersTo : EntityILref = None
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# """The reference to the train detection element in infrastructure."""

