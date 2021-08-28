#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import GradientCurve
from typing import List

#from typing import List, NewType

#Long = NewType("Long", int)

class GradientCurves(object):
	@property
	def GradientCurve(self) -> GradientCurve:
		return self.___gradientCurve
	
	@GradientCurve.setter
	def GradientCurve(self, aGradientCurve : GradientCurve):
		self.___gradientCurve = aGradientCurve

	def create_GradientCurve(self):
		if self.GradientCurve == None:
			self.GradientCurve = []
		self.GradientCurve.append(GradientCurve.GradientCurve())

	def __init__(self):
		self.___gradientCurve : GradientCurve = GradientCurve.GradientCurve()
		# @AssociationType Infrastructure.GradientCurve*
		# @AssociationMultiplicity 1..*

