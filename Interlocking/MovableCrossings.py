#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import MovableCrossing
from typing import List

class MovableCrossings(object):
	@property
	def MovableCrossing(self) -> MovableCrossing:
		return self.___movableCrossing
	
	@MovableCrossing.setter
	def MovableCrossing(self, aMovableCrossing : MovableCrossing):
		self.___movableCrossing = aMovableCrossing

	def __init__(self):
		self.___movableCrossing : MovableCrossing = None
		# @AssociationType Interlocking.MovableCrossing*
		# @AssociationMultiplicity 1..*
		# """Crossings are a special item for interlockings as a position is required for them even if there is no really movable item trackside. Here the functional aspects for interlocking operation are considered."""