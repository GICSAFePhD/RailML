#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import DangerPoint
from typing import List

class DangerPoints(object):
	"""container element for all DangerPoint elements"""
	@property
	def DangerPoint(self) -> DangerPoint:
		return self.___dangerPoint
	
	@DangerPoint.setter
	def DangerPoint(self, *aDangerPoint : DangerPoint):
		self.___dangerPoint = aDangerPoint

	def __init__(self):
		self.___dangerPoint : DangerPoint = DangerPoint.DangerPoint()
		# @AssociationType Interlocking.DangerPoint*
		# @AssociationMultiplicity 1..*
		# """position beyond the exit signal up to where a train is likely to be safe"""

