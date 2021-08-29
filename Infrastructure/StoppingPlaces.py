#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import StoppingPlace
from typing import List

class StoppingPlaces(object):
	@property
	def StoppingPlace(self) -> StoppingPlace:
		return self.___stoppingPlace
	
	@StoppingPlace.setter
	def StoppingPlace(self, *aStoppingPlace : StoppingPlace):
		self.___stoppingPlace = aStoppingPlace

	def create_StoppingPlace(self):
		if self.StoppingPlace == None:
			self.StoppingPlace = []
		self.StoppingPlace.append(StoppingPlace.StoppingPlace())

	def __init__(self):
		self.___stoppingPlace : StoppingPlace = None
		# @AssociationType Infrastructure.StoppingPlace*
		# @AssociationMultiplicity 1..*

