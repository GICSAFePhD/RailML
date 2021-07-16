#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking.MovableCrossing import MovableCrossing
from typing import List

class MovableCrossings(object):
	def setMovableCrossing(self, *aMovableCrossing : MovableCrossing):
		self._movableCrossing = aMovableCrossing

	def getMovableCrossing(self) -> MovableCrossing:
		return self._movableCrossing

	def __init__(self):
		self._movableCrossing : MovableCrossing = None
		# @AssociationType Interlocking.MovableCrossing*
		# @AssociationMultiplicity 1..*
		# """Crossings are a special item for interlockings as a position is required for them even if there is no really movable item trackside. Here the functional aspects for interlocking operation are considered."""

