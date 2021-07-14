#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure.WeightLimit import WeightLimit
from typing import List

class WeightLimits(object):
	"""umbrella element for all weightLimit elements"""
	def setWeightLimit(self, *aWeightLimit : WeightLimit):
		self._weightLimit = aWeightLimit

	def getWeightLimit(self) -> WeightLimit:
		return self._weightLimit

	def __init__(self):
		self._weightLimit : WeightLimit = None
		# @AssociationType Infrastructure.WeightLimit*
		# @AssociationMultiplicity 1..*

