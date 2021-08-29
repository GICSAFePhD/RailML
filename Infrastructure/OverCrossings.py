#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import OverCrossing
from typing import List

class OverCrossings(object):
	@property
	def OverCrossing(self) -> OverCrossing:
		return self.___overCrossing
	
	@OverCrossing.setter
	def OverCrossing(self, aOverCrossing : OverCrossing):
		self.___overCrossing = aOverCrossing

	def create_OverCrossing(self):
		if self.OverCrossing == None:
			self.OverCrossing = []
		self.OverCrossing.append(OverCrossing.OverCrossing())

	def __init__(self):
		self.___overCrossing : OverCrossing = None
		# @AssociationType Infrastructure.OverCrossing*
		# @AssociationMultiplicity 1..*

