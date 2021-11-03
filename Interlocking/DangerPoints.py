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
	def DangerPoint(self, aDangerPoint : DangerPoint):	# *aDangerPoint
		self.___dangerPoint = aDangerPoint

	def create_DangerPoint(self):
		if self.DangerPoint == None:
			self.DangerPoint = []
		self.DangerPoint.append(DangerPoint.DangerPoint())

	def __init__(self):
		self.___dangerPoint : DangerPoint = None
		# @AssociationType Interlocking.DangerPoint*
		# @AssociationMultiplicity 1..*
		# """position beyond the exit signal up to where a train is likely to be safe"""