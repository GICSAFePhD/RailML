#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import UnderCrossing
from typing import List

class UnderCrossings(object):
	@property
	def UnderCrossing(self) -> UnderCrossing:
		return self.___gradientCurve
	
	@UnderCrossing.setter
	def UnderCrossing(self, *aUnderCrossing : UnderCrossing):
		self.___gradientCurve = aUnderCrossing

	def __init__(self):
		self.___underCrossing : UnderCrossing = UnderCrossing.UnderCrossing()
		# @AssociationType Infrastructure.UnderCrossing*
		# @AssociationMultiplicity 1..*

