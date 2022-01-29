#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import UnderCrossing
from typing import List

class UnderCrossings(object):
	@property
	def UnderCrossing(self) -> UnderCrossing:
		return self.___underCrossing
	
	@UnderCrossing.setter
	def UnderCrossing(self, aUnderCrossing : UnderCrossing):	#TODO *aUnderCrossing
		self.___underCrossing = aUnderCrossing

	def create_UnderCrossing(self):
		if self.UnderCrossing == None:
			self.UnderCrossing = []
		self.UnderCrossing.append(UnderCrossing.UnderCrossing())

	def __init__(self):
		self.___underCrossing : UnderCrossing = None
		# @AssociationType Infrastructure.UnderCrossing*
		# @AssociationMultiplicity 1..*

