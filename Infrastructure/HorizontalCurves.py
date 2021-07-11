#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import HorizontalCurve
from typing import List

class HorizontalCurves(object):
	def setHorizontalCurve(self, aHorizontalCurve : HorizontalCurve):
		self._horizontalCurve = aHorizontalCurve

	def getHorizontalCurve(self) -> HorizontalCurve:
		return self._horizontalCurve

	def __init__(self):
		self._horizontalCurve : HorizontalCurve = None
		# @AssociationType Infrastructure.HorizontalCurve*
		# @AssociationMultiplicity 1..*

