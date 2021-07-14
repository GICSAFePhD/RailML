#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure.OverCrossing import OverCrossing
from typing import List

class OverCrossings(object):
	def setOverCrossing(self, *aOverCrossing : OverCrossing):
		self._overCrossing = aOverCrossing

	def getOverCrossing(self) -> OverCrossing:
		return self._overCrossing

	def __init__(self):
		self._overCrossing : OverCrossing = None
		# @AssociationType Infrastructure.OverCrossing*
		# @AssociationMultiplicity 1..*

