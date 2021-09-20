#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import AspectRelation, EntityIL
from typing import List

class SignalPlan(EntityIL.EntityIL):
	"""The signalplan describes a set of aspect relations. 
	In speed signalling systems, the aspect relation between signals represents a speed profile that the train must respect."""
	@property
	def AspectRelation(self) -> AspectRelation:
		return self.___aspectRelation
	
	@AspectRelation.setter
	def AspectRelation(self, aAspectRelation : AspectRelation):	# TODO *aAspectRelation
		self.___aspectRelation = aAspectRelation

	def create_AspectRelation(self):
		if self.AspectRelation == None:
			self.AspectRelation = []
		self.AspectRelation.append(AspectRelation.AspectRelation())
	
	def __init__(self):
		super().__init__()
		self.___aspectRelation : AspectRelation = None
		# @AssociationType Interlocking.AspectRelation*
		# @AssociationMultiplicity 1..*