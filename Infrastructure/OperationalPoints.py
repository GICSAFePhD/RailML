#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Infrastructure import OperationalPoint
from typing import List

class OperationalPoints(object):
	def setOperationalPoint(self, *aOperationalPoint : OperationalPoint*):
		self._operationalPoint = aOperationalPoint

	def getOperationalPoint(self) -> OperationalPoint*:
		return self._operationalPoint

	def __init__(self):
		self._operationalPoint : OperationalPoint = None
		# @AssociationType Infrastructure.OperationalPoint*
		# @AssociationMultiplicity 1..*

