#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure.StoppingPlace import StoppingPlace
from typing import List

class StoppingPlaces(object):
	def setStoppingPlace(self, *aStoppingPlace : StoppingPlace):
		self._stoppingPlace = aStoppingPlace

	def getStoppingPlace(self) -> StoppingPlace:
		return self._stoppingPlace

	def __init__(self):
		self._stoppingPlace : StoppingPlace = None
		# @AssociationType Infrastructure.StoppingPlace*
		# @AssociationMultiplicity 1..*

