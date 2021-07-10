#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Interlocking import DangerPoint
from typing import List

class DangerPoints(object):
	"""container element for all DangerPoint elements"""
	def setDangerPoint(self, *aDangerPoint : DangerPoint*):
		self._dangerPoint = aDangerPoint

	def getDangerPoint(self) -> DangerPoint*:
		return self._dangerPoint

	def __init__(self):
		self._dangerPoint : DangerPoint = None
		# @AssociationType Interlocking.DangerPoint*
		# @AssociationMultiplicity 1..*
		# """position beyond the exit signal up to where a train is likely to be safe"""

