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

	def __init__(self):
		self.___stoppingPlace : StoppingPlace = StoppingPlace.StoppingPlace()
		# @AssociationType Infrastructure.StoppingPlace*
		# @AssociationMultiplicity 1..*

