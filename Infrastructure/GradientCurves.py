#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import GradientCurve
from typing import List

class GradientCurves(object):
	def setGradientCurve(self, aGradientCurve : GradientCurve):
		self._gradientCurve = aGradientCurve

	def getGradientCurve(self) -> GradientCurve:
		return self._gradientCurve

	def __init__(self):
		self._gradientCurve : GradientCurve = None
		# @AssociationType Infrastructure.GradientCurve*
		# @AssociationMultiplicity 1..*

