#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking.AspectRelation import AspectRelation
from RailML.Interlocking.EntityIL import EntityIL
from typing import List

class SignalPlan(EntityIL):
	"""The signalplan describes a set of aspect relations. 
	In speed signalling systems, the aspect relation between signals represents a speed profile that the train must respect."""
	def setAspectRelation(self, *aAspectRelation : AspectRelation):
		self._aspectRelation = aAspectRelation

	def getAspectRelation(self) -> AspectRelation:
		return self._aspectRelation

	def __init__(self):
		self._aspectRelation : AspectRelation = None
		# @AssociationType Interlocking.AspectRelation*
		# @AssociationMultiplicity 1..*

