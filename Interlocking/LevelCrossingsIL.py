#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking.LevelCrossingIL import LevelCrossingIL
from typing import List

class LevelCrossingsIL(object):
	"""container element for all LevelCrossingIL elements"""
	def setLevelCrossingIL(self, *aLevelCrossingIL : LevelCrossingIL):
		self._levelCrossingIL = aLevelCrossingIL

	def getLevelCrossingIL(self) -> LevelCrossingIL:
		return self._levelCrossingIL

	def __init__(self):
		self._levelCrossingIL : LevelCrossingIL = None
		# @AssociationType Interlocking.LevelCrossingIL*
		# @AssociationMultiplicity 1..*
		# """The level crossing is a track asset allowing road traffic to cross the railway track in a secure way on the same level. Here the functional aspects for interlocking operation are considered."""

