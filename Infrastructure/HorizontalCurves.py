#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import HorizontalCurve
from typing import List

class HorizontalCurves(object):
	@property
	def HorizontalCurve(self) -> HorizontalCurve:
		return self.___horizontalCurve
	
	@HorizontalCurve.setter
	def HorizontalCurve(self, aHorizontalCurve : HorizontalCurve):
		self.___horizontalCurve = aHorizontalCurve

	def create_HorizontalCurve(self):
		if self.HorizontalCurve == None:
			self.HorizontalCurve = []
		self.HorizontalCurve.append(HorizontalCurve.HorizontalCurve())

	def __init__(self):
		self.___horizontalCurve : HorizontalCurve = None
		# @AssociationType Infrastructure.HorizontalCurve*
		# @AssociationMultiplicity 1..*

