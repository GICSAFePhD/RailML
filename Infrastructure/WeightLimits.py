#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import WeightLimit
from typing import List

class WeightLimits(object):
	"""umbrella element for all weightLimit elements"""
	@property
	def WeightLimit(self) -> WeightLimit:
		return self.___weightLimit
	
	@WeightLimit.setter
	def WeightLimit(self, *aWeightLimit : WeightLimit):
		self.___weightLimit = aWeightLimit

	def create_WeightLimit(self):
		if self.WeightLimit == None:
			self.WeightLimit = []
		self.WeightLimit.append(WeightLimit.WeightLimit())

	def __init__(self):
		self.___weightLimit : WeightLimit = None
		# @AssociationType Infrastructure.WeightLimit*
		# @AssociationMultiplicity 1..*