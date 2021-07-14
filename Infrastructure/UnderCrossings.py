#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure.UnderCrossing import UnderCrossing
from typing import List

class UnderCrossings(object):
	def setUnderCrossing(self, *aUnderCrossing : UnderCrossing):
		self._underCrossing = aUnderCrossing

	def getUnderCrossing(self) -> UnderCrossing:
		return self._underCrossing

	def __init__(self):
		self._underCrossing : UnderCrossing = None
		# @AssociationType Infrastructure.UnderCrossing*
		# @AssociationMultiplicity 1..*

