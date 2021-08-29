#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import OperationalPoint
from typing import List

class OperationalPoints(object):
	@property
	def OperationalPoint(self) -> OperationalPoint:
		return self.___operationalPoint
	
	@OperationalPoint.setter
	def OperationalPoint(self, aOperationalPoint : OperationalPoint):
		self.___operationalPoint = aOperationalPoint

	def create_OperationalPoint(self):
		if self.OperationalPoint == None:
			self.OperationalPoint = []
		self.OperationalPoint.append(OperationalPoint.OperationalPoint())

	def __init__(self):
		self.___operationalPoint : OperationalPoint = None
		# @AssociationType Infrastructure.OperationalPoint*
		# @AssociationMultiplicity 1..*

