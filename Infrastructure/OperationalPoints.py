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

	def __init__(self):
		self.___operationalPoint : OperationalPoint = OperationalPoint.OperationalPoint()
		# @AssociationType Infrastructure.OperationalPoint*
		# @AssociationMultiplicity 1..*

